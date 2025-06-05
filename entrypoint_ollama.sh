#!/bin/sh
set -e

# Charge les variables de l'environnement si le fichier existe
[ -f .env ] && . .env

MODELS=""
[ -n "$OLLAMA_TEXT_MODEL" ] && MODELS="$MODELS $OLLAMA_TEXT_MODEL"
[ -n "$OLLAMA_IMAGE_MODEL" ] && MODELS="$MODELS $OLLAMA_IMAGE_MODEL"

# Télécharge les modèles en utilisant docker compose (mode hôte)
download_models_host() {
  for MODEL in $MODELS; do
    [ -z "$MODEL" ] && continue
    if docker compose run --rm --entrypoint ollama ollama list | grep -q "^$MODEL"; then
      echo "Model $MODEL already present."
    else
      echo "Downloading $MODEL..."
      docker compose run --rm --entrypoint ollama ollama pull "$MODEL"
    fi
  done
}

# Télécharge un modèle à l'intérieur du conteneur
pull_model_container() {
  MODEL_NAME="$1"
  [ -z "$MODEL_NAME" ] && return
  if ! /bin/ollama list | grep -q "$MODEL_NAME"; then
    echo "Model $MODEL_NAME not found, downloading..."
    /bin/ollama pull "$MODEL_NAME" | while IFS= read -r line; do
      echo "$line"
      percent=$(echo "$line" | grep -Eo '[0-9]{1,3}%')
      if [ -n "$percent" ]; then
        p=${percent%%%}
        bar=$(printf '%0.s#' $(seq 1 $((p/2))))
        printf "[%-50s] %3s%%\n" "$bar" "$p"
      fi
    done
    echo
    if ! /bin/ollama list | grep -q "$MODEL_NAME"; then
      echo "Error: model $MODEL_NAME failed to download. Exiting."
      exit 1
    fi
  else
    echo "Model $MODEL_NAME already present."
  fi
}

# Si l'argument --download est présent, on télécharge juste les modèles
if [ "$1" = "--download" ]; then
  download_models_host
  exit 0
fi

# Sinon on agit comme entrypoint du conteneur
/bin/ollama serve &
OLLAMA_PID=$!

echo "Waiting for Ollama daemon to be ready..."
until curl -s http://localhost:11434/api/tags > /dev/null; do
  sleep 1
done

for MODEL in $MODELS; do
  pull_model_container "$MODEL"
done

wait $OLLAMA_PID
