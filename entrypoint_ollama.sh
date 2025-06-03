#!/bin/sh
set -e

MODEL="${OLLAMA_TEXT_MODEL:-llama3:8b}"

# Démarre ollama serve en foreground (pour Docker health/lifecycle)
/bin/ollama serve &
OLLAMA_PID=$!

# Attend que le daemon soit prêt
echo "Waiting for Ollama daemon to be ready..."
until curl -s http://localhost:11434/api/tags > /dev/null; do
  sleep 1
done

# Télécharge le modèle si besoin, avec affichage de la progression
if ! /bin/ollama list | grep -q "$MODEL"; then
  echo "Model $MODEL not found, downloading..."
  /bin/ollama pull "$MODEL" | while IFS= read -r line; do
    echo "$line"
    percent=$(echo "$line" | grep -Eo '[0-9]{1,3}%')
    if [ -n "$percent" ]; then
      p=${percent%%%}
      bar=$(printf '%0.s#' $(seq 1 $((p/2))))
      printf "\r[%-50s] %3s%%" "$bar" "$p"
    fi
  done
  echo
else
  echo "Model $MODEL already present."
fi

# Attend la fin du processus principal (ollama serve)
wait $OLLAMA_PID
