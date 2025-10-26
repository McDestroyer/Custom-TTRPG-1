extends Node2D

var map_item_scene = preload("res://MapAssets/base_map_item.tscn")

var held: TextureRect
var dragging_start: Vector2
var drag_cam_start: Vector2
var dragging: bool = false

var map: Array

func _ready() -> void:
	held = map_item_scene.instantiate()
	held.modulate = Color(1, 1, 1, .5)
	$MapLayers.add_child(held)

func _input(event: InputEvent) -> void:
	if event is InputEventMouseMotion:
		var rel_pos = event.position / $Camera2D.zoom.x + $Camera2D.position
		held.position.x =  floor(rel_pos.x / held.size.x) * held.size.x
		held.position.y = floor(rel_pos.y / held.size.y) * held.size.y

		if dragging:
			if Input.is_mouse_button_pressed(MOUSE_BUTTON_MIDDLE):
				$Camera2D.position = drag_cam_start + (dragging_start - event.position) / $Camera2D.zoom.x
			else:
				dragging = false
	elif event is InputEventMouseButton and event.pressed:
		if event.button_index == MOUSE_BUTTON_LEFT:
			var rel_pos = event.position / $Camera2D.zoom.x + $Camera2D.position
			place_item(rel_pos)
		elif event.button_index == MOUSE_BUTTON_MIDDLE:
			dragging_start = event.position
			drag_cam_start = $Camera2D.position
			dragging = true
		elif event.button_index == MOUSE_BUTTON_WHEEL_UP:
			#var zoom_pos: Vector2 = get_global_mouse_position()
			var zoom_scale: float = 1.5 ** (event.factor if event.factor else 1.0)
			$Camera2D.zoom *= zoom_scale
		elif event.button_index == MOUSE_BUTTON_WHEEL_DOWN:
			#var zoom_pos: Vector2 = get_global_mouse_position()
			var zoom_scale: float = 1.5 ** (-event.factor if event.factor else -1.0)
			$Camera2D.zoom *= zoom_scale

func place_item(pos):
	held.modulate = Color(1, 1, 1, 1)

	held = map_item_scene.instantiate()
	held.modulate = Color(1, 1, 1, .5)
	$MapLayers.add_child(held)
	#held.position = pos // held.size.x
	held.position.x = floor(pos.x / held.size.x) * held.size.x
	held.position.y = floor(pos.y / held.size.y) * held.size.y
