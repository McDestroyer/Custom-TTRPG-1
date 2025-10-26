extends Control

# Submenu options
var create_menu_scene = preload("res://SetupMenus/create_menu.tscn").instantiate()
var load_menu_scene = preload("res://SetupMenus/load_menu.tscn").instantiate()
var connect_menu_scene = preload("res://SetupMenus/connect_menu.tscn").instantiate()
@onready
var start_menu_scene = get_tree().root.get_child(1)

# Shorthand Node links
@onready
var CREATE = $CenterContainer/VBoxContainer/Create
@onready
var LOAD = $CenterContainer/VBoxContainer/Load
@onready
var CONNECT = $CenterContainer/VBoxContainer/Connect
@onready
var SETTINGS = $CenterContainer/VBoxContainer/Settings
@onready
var NOTE = $CenterContainer/VBoxContainer/SettingsNote

func _ready() -> void:
	create_menu_scene.start = start_menu_scene
	load_menu_scene.start = start_menu_scene
	connect_menu_scene.start = start_menu_scene
	#SETTINGS.start = start_menu_scene


func _on_create_button_up() -> void:
	Tools.change_scene_to_node(create_menu_scene)


func _on_load_button_up() -> void:
	Tools.change_scene_to_node(load_menu_scene)


func _on_connect_button_up() -> void:
	Tools.change_scene_to_node(connect_menu_scene)


func _on_settings_button_up() -> void:
	$CenterContainer/VBoxContainer/SettingsNote.visible = true
