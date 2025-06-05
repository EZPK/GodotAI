#!/bin/sh
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
[ -f "$SCRIPT_DIR/.env" ] && . "$SCRIPT_DIR/.env"

MODELS=""
[ -n "$OLLAMA_TEXT_MODEL" ] && MODELS="$MODELS $OLLAMA_TEXT_MODEL"
[ -n "$STABLEDIFFUSION_MODEL" ] && MODELS="$MODELS $STABLEDIFFUSION_MODEL"

# Télécharge un modèle à l'intérieur du conteneur
pull_model_container() {
  MODEL_NAME="$1"
  [ -z "$MODEL_NAME" ] && return
  if ! /bin/ollama list | grep -q "$MODEL_NAME"; then
    echo "⏬ Téléchargement du modèle '$MODEL_NAME' en cours..."
    start_time=$(date +%s)
    /bin/ollama pull "$MODEL_NAME" | while IFS= read -r line; do
      percent=$(echo "$line" | grep -Eo '[0-9]{1,3}%')
      if [ -n "$percent" ]; then
        p=${percent%%%}
        bar=$(printf '%0.s#' $(seq 1 $((p/2))))
        elapsed=$(( $(date +%s) - start_time ))
        printf "\r[%-50s] %3s%% | %ds écoulées" "$bar" "$p" "$elapsed"
      fi
    done
    echo
    end_time=$(date +%s)
    duration=$((end_time - start_time))
    if ! /bin/ollama list | grep -q "$MODEL_NAME"; then
      echo "❌ Erreur : le modèle '$MODEL_NAME' n'a pas pu être téléchargé."
      exit 1
    else
      echo "✅ Modèle '$MODEL_NAME' téléchargé en $duration secondes."
    fi
  else
    echo "✔️ Modèle '$MODEL_NAME' déjà présent."
  fi
}

# Si l'argument --download est présent, on ne fait rien (plus de pull côté hôte)
if [ "$1" = "--download" ]; then
  echo "No-op: download only handled inside the container."
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