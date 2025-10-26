extends Control

## Whether a character can walk through the tile
var effects: Array[MapItemEffect] = []
## 
var overlays: Array[ColorRect]
var tilesize: Vector2i
var sublayer: MapScaleLayer

class MapItemEffect:
	pass

func setup(
		icon: Image, tile_size: Vector2i = Vector2i(1, 1), 
		overlay_array: Array[ColorRect] = [], effect_array: Array[MapItemEffect] = [],
		submaplayer: MapScaleLayer = null) -> void:
	$Icon.texture = icon
	self.size = Vector2i(128, 128)
	effects = effect_array
	overlays = overlay_array
	tilesize = tile_size
	sublayer = submaplayer
