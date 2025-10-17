extends Node

func _onready() -> void:
	get_tree().get_root().files_dropped.connect(_on_files_dropped)

func _on_files_dropped(file_paths: PackedStringArray) -> void:
	# Access the files with the given file paths and use them somehow
	print(file_paths)
