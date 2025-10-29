import util
import math
import variables
import water

def dinasor():
	direction = North
	vertical = { North: South, South: North }

	change_hat(Hats.Dinosaur_Hat)

	while True:
		if not can_move(direction):
			change_hat(Hats.Purple_Hat)
			change_hat(Hats.Dinosaur_Hat)
			direction = vertical[direction]
		move(direction)