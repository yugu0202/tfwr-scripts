import util
import math
import variables
import water
import fertilizer

def main(line, entity, harvest_func, plant_func):
	horizontal_direction = East
	horizontal = { East: West, West: East }
	
	while True:
		tree_line_counted = False
		y = get_pos_y()
		fertilizer.use_fertilizer()
		if can_harvest():
			harvest_func()
		plant_func(line, entity)
		water.use_water()
		variables.random_fertilizer_func()
		move(horizontal_direction)
