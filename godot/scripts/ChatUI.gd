extends Control

@onready var chat_history: RichTextLabel = $GridContainer/BottomLeft/BoxContainer/ChatHistory
@onready var input_box: LineEdit = $GridContainer/BottomLeft/BoxContainer/HBoxContainer/InputBox
@onready var send_button: Button = $GridContainer/BottomLeft/BoxContainer/HBoxContainer/SendButton

var websocket := WebSocketClient.new()
var is_streaming := false

func _ready():
        var err = websocket.connect_to_url("ws://localhost:8000/ws")
        if err != OK:
                printerr("[ChatUI] WebSocket connection failed: %s" % err)
        websocket.connect("connection_established", Callable(self, "_on_ws_connected"))
        websocket.connect("connection_error", Callable(self, "_on_ws_error"))
        websocket.connect("connection_closed", Callable(self, "_on_ws_closed"))
        websocket.connect("data_received", Callable(self, "_on_ws_data"))
	
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
        if is_streaming or input_box.text.strip_edges() == "":
                return
        var user_message = input_box.text.strip_edges()
        _append_message("Vous", user_message)
        input_box.text = ""
        _send_to_llm(user_message)

func _send_to_llm(message: String):
        if websocket.get_connection_status() != WebSocketClient.CONNECTION_CONNECTED:
                _append_message("Assistant", "[WebSocket non connecté]")
                return
        var body := {"prompt": message}
        websocket.get_peer(1).put_packet(JSON.stringify(body).to_utf8())
        is_streaming = true

func _on_ws_connected(protocol: String) -> void:
        pass

func _on_ws_error() -> void:
        printerr("[ChatUI] WebSocket connection error")

func _on_ws_closed(was_clean: bool) -> void:
        printerr("[ChatUI] WebSocket closed")

func _on_ws_data() -> void:
        while websocket.get_peer(1).get_available_packet_count() > 0:
                var line = websocket.get_peer(1).get_packet().get_string_from_utf8().strip_edges()
                if line == "[DONE]":
                        is_streaming = false
                        _append_message("Assistant", chat_history.text.split("Assistant: ")[-1])
                        continue
                var json := JSON.new()
                if json.parse(line) == OK:
                        var token := str(json.data.get("response", ""))
                        if is_instance_valid(chat_history):
                                var current = chat_history.text.split("Assistant: ")[-1]
                                chat_history.text = _format_chat("Assistant", current + token)
                else:
                        printerr("Erreur parsing ligne: ", line)

func _process(delta: float) -> void:
        if websocket.get_connection_status() != WebSocketClient.CONNECTION_DISCONNECTED:
                websocket.poll()

func _append_message(who: String, msg: String):
	chat_history.append_text("%s: %s\n" % [who, msg])
	chat_history.scroll_to_line(chat_history.get_line_count())

func _format_chat(who: String, msg: String) -> String:
	return "%s: %s" % [who, msg]
