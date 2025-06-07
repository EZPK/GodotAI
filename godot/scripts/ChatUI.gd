extends Control

@onready var chat_history: RichTextLabel = $GridContainer/BottomLeft/BoxContainer/ChatHistory
@onready var input_box: LineEdit = $GridContainer/BottomLeft/BoxContainer/HBoxContainer/InputBox
@onready var send_button: Button = $GridContainer/BottomLeft/BoxContainer/HBoxContainer/SendButton

var http := HTTPRequest.new()
var stream_timer := Timer.new()
var stream_buffer := ""
var stream_lines := []
var line_index := 0
var is_streaming := false
var live_assistant_response := ""
var chat_lines := [] # Historique du chat

const USER_EMOJI := "🧑"
const ASSISTANT_EMOJI := "🤖"

func _ready():
	add_child(http)
	add_child(stream_timer)
	stream_timer.one_shot = false
	stream_timer.wait_time = 0.03
	stream_timer.timeout.connect(_on_stream_timer_timeout)
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
		_append_message("", "Bonjour ! Posez-moi une question.")
	else:
		printerr("[ChatUI] chat_history n'est pas instancié !")

func _on_send_pressed(_event: Variant = null):
	if is_streaming or input_box.text.strip_edges() == "":
		return
	var user_message = input_box.text.strip_edges()
	_append_message("Vous", user_message)
	input_box.text = ""
	_send_to_llm(user_message)

func _send_to_llm(message: String):
	var url := "http://localhost:8000/txt"
	var body := {
		"prompt": message,
		"stream": false, # active le streaming
	}
	var headers := ["Content-Type: application/json"]
	var err := http.request(url, headers, HTTPClient.METHOD_POST, JSON.stringify(body))
	if err != OK:
		_append_message("Assistant", "[Erreur réseau]")
	else:
		stream_buffer = ""
		stream_lines.clear()
		line_index = 0
		is_streaming = true
		live_assistant_response = ""
		chat_lines.append("%s : " % ASSISTANT_EMOJI) # Ligne vide pour la réponse
		_refresh_chat_history()

func _on_result(_result, _code, _headers, body):
	stream_buffer = body.get_string_from_utf8()
	stream_lines = stream_buffer.split("\n")
	line_index = 0
	stream_timer.start()

func _on_stream_timer_timeout():
	if line_index >= stream_lines.size():
		stream_timer.stop()
		is_streaming = false
		# À la fin, on fige la réponse finale dans la dernière ligne
		if chat_lines.size() > 0:
			chat_lines[chat_lines.size() - 1] = "%s : %s" % [ASSISTANT_EMOJI, live_assistant_response]
			_refresh_chat_history()
		return

	var line = stream_lines[line_index].strip_edges()
	line_index += 1
	if line == "":
		return

	var json := JSON.new()
	if json.parse(line) == OK:
		var token := str(json.data.get("response", ""))
		live_assistant_response += token
		if chat_lines.size() > 0:
			chat_lines[chat_lines.size() - 1] = "%s : %s" % [ASSISTANT_EMOJI, live_assistant_response]
			_refresh_chat_history()
	else:
		printerr("Erreur parsing ligne: ", line)

func _append_message(who: String, msg: String):
	var emoji = USER_EMOJI if who == "Vous" else ASSISTANT_EMOJI
	chat_lines.append("%s %s: %s" % [emoji, who, msg])
	_refresh_chat_history()

func _refresh_chat_history():
	chat_history.text = String("\n").join(chat_lines)
