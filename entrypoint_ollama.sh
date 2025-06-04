#!/bin/sh
set -e

MODEL_TEXT="${OLLAMA_TEXT_MODEL:-llama3:8b}"
MODEL_IMAGE="${OLLAMA_IMAGE_MODEL:-stable-diffusion}"  # Peut être vide si non défini

# Démarre ollama serve en foreground (pour Docker health/lifecycle)
/bin/ollama serve &
OLLAMA_PID=$!

# Attend que le daemon soit prêt
echo "Waiting for Ollama daemon to be ready..."
until curl -s http://localhost:11434/api/tags > /dev/null; do
  sleep 1
done

download_model() {
  MODEL_NAME="$1"
  if [ -z "$MODEL_NAME" ]; then
    return
  fi
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

download_model "$MODEL_TEXT"
download_model "$MODEL_IMAGE"

# Attend la fin du processus principal (ollama serve)
wait $OLLAMA_PID
