extends Node
class_name MapScaleLayer

var map_grid: Array[Array]  # [Element]

class Element:
	pass


"""
WorldMap
[
	MapScale
	[
		Layer
		[
			Tile (subTile or mainTile)
		]
	]
]

WorldMap contains a List
"""
