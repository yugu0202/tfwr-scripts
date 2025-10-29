

def run():
	direction = [North, East, South, West]
	index = 0
	while True:
		if get_entity_type() == Entities.Treasure:
			harvest()
			break

		if can_move(direction[index]):
			move(direction[index])
		else:
			index = (index + 1) % 4
		