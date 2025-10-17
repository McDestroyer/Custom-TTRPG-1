extends Node2D

@onready var tilemap_layer = $TileMapLayer

func _ready() -> void:
	# Step 1: Load the image dynamically
	var image = Image.new()
	var image_path = "res://icon.svg"  # Replace with your image path
	if image.load(image_path) != OK:
		print("Failed to load image!")
		return

	# Step 2: Create an ImageTexture from the loaded image
	var texture = ImageTexture.new()
	texture.create_from_image(image)

	# Step 3: Create a new TileSet and add the texture as a tile
	var tileset = TileSet.new()
	#tileset.add_source()
	var tile_id = tileset.create_tile(0)  # Create a tile with ID 0
	tileset.tile_set_texture(tile_id, texture)

	# Step 4: Assign the TileSet to the TileMapLayer
	tilemap_layer.tile_set = tileset

	# Step 5: Add the tile to the TileMapLayer at a specific position
	var position = Vector2(2, 3)  # Replace with your desired tilemap coordinates
	tilemap_layer.set_cell(position, 0)  # Layer 0, position (2, 3), tile ID 0
