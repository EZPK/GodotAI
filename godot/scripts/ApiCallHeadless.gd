extends Node

@onready var response_label: Label = $VBoxContainer/Label

func _ready():
	print("[🧠] Appel API Godot avec interface graphique...")

	var http := HTTPRequest.new()
	add_child(http)

	http.request_completed.connect(_on_result)

	var url := "http://localhost:11434/api/generate"
	var body := {
		"model": "tinyllama:latest",
		"prompt": "maximum 10mots Dis bonjour au user en français",
		"stream": true,
		"num_predict": 10
	}
	var headers := ["Content-Type: application/json"]
	var err := http.request(url, headers, HTTPClient.METHOD_POST, JSON.stringify(body))
	if err != OK:
		printerr("❌ Erreur HTTP: ", err)

func _on_result(_result: int, _code: int, _headers: PackedStringArray, body: PackedByteArray):
	var response_text := ""
	var raw_text := body.get_string_from_utf8()
	print("📦 Réponse brute:")
	for line in raw_text.split("\n"):
		if line.strip_edges() == "":
			continue
		var json := JSON.new()
		if json.parse(line) == OK:
			var segment = str(json.data.get("response", ""))
			response_text += segment
		else:
			printerr("❌ Erreur de parsing JSON sur la ligne:", line)

	print("✅ Texte complet reçu:\n" + response_text + "\n")
	response_label.text = response_text
