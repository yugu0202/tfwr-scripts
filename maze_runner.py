

def run():
	direction = [North, East, South, West]
	index = 0
	while True:
		if get_entity_type() == Entities.Treasure:
			harvest()
			break
		
		# 左向きのインデックス
		left_index = (index + 3) % 4
		if can_move(direction[left_index]):
			move(direction[left_index])
			index = left_index
			continue

		if can_move(direction[index]):
			move(direction[index])
		else:
			index = (index + 1) % 4
		