extends SceneTree

# Instance HTTPRequest pour les appels API
var http := HTTPRequest.new()
# Texte partiel accumulé lors du streaming
var partial_text := ""
# Timestamps pour monitoring
var t_start_request := 0
var t_request_sent := 0
var t_response_received := 0
var t_response_displayed := 0

func _initialize():
        # Préparation du modèle et du prompt
	var model = "god:latest"
	print("[🧠] Appel API Godot avec interface graphique en streaming...")
	print("[🧠] Modèle utilisé : ", model)
	# Timestamp début
	t_start_request = Time.get_ticks_msec()
	print("⌛ Début de la requête : ", t_start_request)

        # Ajout du noeud HTTPRequest à la scène
        get_root().add_child(http)
	# Connexion du signal de complétion
	http.request_completed.connect(_on_result)

	# Construction de la requête API
	var url := "http://localhost:11434/api/generate"
	var body := {
		"model": model,
		"prompt": "Bonjour ? Peux tu te décrires ? Qui es tu, quel est ton but ?",
		"stream": true,
		"num_predict": 10,
	}
	var headers := ["Content-Type: application/json"]
	# Envoi de la requête HTTP POST
	var err := http.request(url, headers, HTTPClient.METHOD_POST, JSON.stringify(body))
	if err != OK:
		printerr("❌ Erreur HTTP: ", err)
	else:
		t_request_sent = Time.get_ticks_msec()
		print("🚀 Requête HTTP envoyée à : ", t_request_sent, " (delta : ", t_request_sent - t_start_request, " ms)")

# Callback appelé à la réception de la réponse HTTP
func _on_result(_result: int, _code: int, _headers: PackedStringArray, body: PackedByteArray):
	t_response_received = Time.get_ticks_msec()
	print("📦 Réponse reçue à : ", t_response_received, " (delta : ", t_response_received - t_request_sent, " ms depuis envoi)")
	print("Body size: ", body.size())

	# Décodage explicite en UTF-8
	var all_text := body.get_string_from_utf8()
	# Monitoring du nombre de lignes JSON reçues
	var line_count := 0
	for line in all_text.split("\n"):
		line = line.strip_edges()
		if line == "":
			continue
		print("Ligne reçue: ", line)
		line_count += 1

		# Parsing JSON ligne par ligne
		var json := JSON.new()
		var err := json.parse(line)
		if err == OK:
			var token := str(json.data.get("response", ""))
			partial_text += token
                        print(token)
		else:
			printerr("❌ JSON invalide :", line)

	t_response_displayed = Time.get_ticks_msec()
	print("✅ Texte complet reçu à : ", t_response_displayed, " (delta : ", t_response_displayed - t_response_received, " ms depuis réception)")
	print("⏱️ Temps total (requête -> affichage) : ", t_response_displayed - t_start_request, " ms")
	print("⏱️ Nombre de lignes JSON traitées : ", line_count)
        print("\n---\nTexte final affiché :\n" + partial_text)
        quit()
