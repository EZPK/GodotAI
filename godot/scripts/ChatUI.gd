extends Control

# Script pour une interface de chat simple avec le LLM
@onready var chat_history: RichTextLabel = $BottomLeft/VBoxContainer/ChatHistory
@onready var input_box: LineEdit = $BottomLeft/VBoxContainer/HBoxContainer/InputBox
@onready var send_button: Button = $BottomLeft/VBoxContainer/HBoxContainer/SendButton

var conversation: Array = []
var http := HTTPRequest.new()
var is_waiting := false

func _ready():
	add_child(http)
	http.request_completed.connect(_on_result)
	if is_instance_valid(input_box):
		input_box.text_submitted.connect(_on_send_pressed)
	else:
		printerr("[ChatUI] input_box n'est pas instancié !")
	if is_instance_valid(send_button):
		send_button.pressed.connect(_on_send_pressed)
	else:
		printerr("[ChatUI] send_button n'est pas instancié !")
	if is_instance_valid(chat_history):
		chat_history.clear()
		_append_message("Assistant", "Bonjour ! Posez-moi une question.")
	else:
		printerr("[ChatUI] chat_history n'est pas instancié !")

func _on_send_pressed(_event: Variant = null):
	if is_waiting or input_box.text.strip_edges() == "":
		return
	var user_message = input_box.text.strip_edges()
	_append_message("Vous", user_message)
	conversation.append({"role": "user", "content": user_message})
	input_box.text = ""
	is_waiting = true
	_send_to_llm(user_message)

func _send_to_llm(_message: String):
	var url := "http://localhost:11434/api/generate"
	var prompt := _build_prompt()
	var body := {
		"model": "god:latest",
		"prompt": prompt,
		"stream": false,
		"num_predict": 64,
		"temperature": 0.2
	}
	var headers := ["Content-Type: application/json"]
	var err := http.request(url, headers, HTTPClient.METHOD_POST, JSON.stringify(body))
	if err != OK:
		_append_message("Assistant", "[Erreur réseau]")
		is_waiting = false

func _build_prompt() -> String:
	# Concatène l'historique pour donner du contexte au LLM
	var prompt = ""
	for msg in conversation:
		if msg.role == "user":
			prompt += "Utilisateur: %s\n" % msg.content
		else:
			prompt += "Assistant: %s\n" % msg.content
	prompt += "Assistant: "
	return prompt

func _on_result(_result, _code, _headers, body):
	is_waiting = false
	var all_text: String = body.get_string_from_utf8()
	var response := ""
	for line in all_text.split("\n"):
		line = line.strip_edges()
		if line == "":
			continue
		var json := JSON.new()
		if json.parse(line) == OK:
			response += str(json.data.get("response", ""))
	if response.strip_edges() == "":
		response = "[Aucune réponse du LLM]"
	_append_message("Assistant", response)
	conversation.append({"role": "assistant", "content": response})

func _append_message(who: String, msg: String):
	chat_history.append_text("%s: %s\n" % [who, msg])
	chat_history.scroll_to_line(chat_history.get_line_count())
