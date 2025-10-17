extends Node

var boolean: bool:
	set(val):
		boolean = val
		print("Set boolean to ", val)
	get:
		print("I'm lying!")
		return not boolean
