extends Node2D

"
Layers will need the following settings:
	## Determines whether anyone other than the GM can see objects in the layer.
	visible_to_players: bool
	
	## Determines if players can deactivate the visibility of a layer to see or click on what's beneath
	visibility_can_be_toggled: bool
	
	## Determines if players can interact with anything on the layer at all, overrides individual components.
	players_can_interact: bool
	
	## Determines if mouse clicks pass through when players can't interact with the layer or are blocked.
	player_clicks_pass_through: bool
	
	## Determines the order the layers are displayed.
	z_index: int
	
	## Whether objects within should be accounted for when calculating player movement.
	interacts_with_pathing: bool
	
Premade Layers (in order of z-index):
	Map Layer:
		# Background which does interact with pathing and is visible but players cannot interact
		visible_to_players = true
		visibility_can_be_toggled = true
		players_can_interact = false
		z_index: false
		interacts_with_pathing: true
"














var map_item_scene = preload("res://MapAssets/base_map_item.tscn")

var held: TextureRect

var camera: Camera2D
var dragging_start: Vector2
var drag_cam_start: Vector2
var dragging: bool = false

var map: Array

func _ready() -> void:
	camera = get_tree().root.get_camera_2d()
	held = map_item_scene.instantiate()
	held.modulate = Color(1, 1, 1, .5)
	$MapLayers.add_child(held)

func _input(event: InputEvent) -> void:
	if event is InputEventMouseMotion:
		var rel_pos = get_global_mouse_pos(event.position)
		held.position.x =  floor(rel_pos.x / held.size.x) * held.size.x
		held.position.y = floor(rel_pos.y / held.size.y) * held.size.y

		if dragging:
			if Input.is_mouse_button_pressed(MOUSE_BUTTON_MIDDLE):
				camera.position = drag_cam_start + (dragging_start - event.position) / camera.zoom.x
			else:
				dragging = false
	elif event is InputEventMouseButton and event.pressed:
		if event.button_index == MOUSE_BUTTON_LEFT:
			var global_pos = get_global_mouse_pos(event.position)
			place_item(global_pos)
		elif event.button_index == MOUSE_BUTTON_MIDDLE:
			dragging_start = event.position
			drag_cam_start = camera.position
			dragging = true
		elif event.button_index == MOUSE_BUTTON_WHEEL_UP:
			#var zoom_pos: Vector2 = get_global_mouse_position()
			var zoom_scale: float = 1.5 ** (event.factor if event.factor else 1.0)
			camera.zoom *= zoom_scale
		elif event.button_index == MOUSE_BUTTON_WHEEL_DOWN:
			#var zoom_pos: Vector2 = get_global_mouse_position()
			var zoom_scale: float = 1.5 ** (-event.factor if event.factor else -1.0)
			camera.zoom *= zoom_scale

func place_item(pos):
	held.modulate = Color(1, 1, 1, 1)

	held = map_item_scene.instantiate()
	held.modulate = Color(1, 1, 1, .5)
	$MapLayers.add_child(held)
	#held.position = pos // held.size.x
	held.position.x = floor(pos.x / held.size.x) * held.size.x
	held.position.y = floor(pos.y / held.size.y) * held.size.y

## 
func get_global_mouse_pos(screen_pos: Vector2) -> Vector2:
	# Create a temporary variable for the math.
	var temp: Vector2 = screen_pos
	# Make the screen pos relative tot he center rather than the top left due to
	# how the camera is positioned (from the center).
	temp -= camera.get_viewport_rect().size / 2
	# Compensate for the camera's current zoom.
	temp /= camera.zoom.abs()
	# Offset it by the camera's current position to get the global position.
	temp += camera.position
	return temp
	
	# Or, in short:
	#return (screen_pos - camera.get_viewport_rect().size / 2) / camera.zoom.abs() + camera.position
