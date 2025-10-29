import util
import math
import variables
import water
import fertilizer

def main():
	horizontal_direction = East
	horizontal = { East: West, West: East }
	vertical_direction = North
	vertical = { North: South, South: North }
	plant_dict = util.rule_to_plant_dict(variables.plant_rules)
	
	while True:
		tree_line_count = 0
		height = get_world_size() / variables.parallel_vertical_harvest // 1
		for h in range(height):
			tree_line_counted = False
			y = get_pos_y()
			width = get_world_size() / variables.parallel_horizontal_harvest // 1
			for w in range(width):
				fertilizer.use_fertilizer()
				if can_harvest():
					if get_entity_type() == Entities.Bush:
						cost = get_cost(Entities.Hedge)[Items.Weird_Substance]
						use_item(Items.Weird_Substance, cost)
					harvest()
				if y in plant_dict:
					entity = plant_dict[y]
					if entity == Entities.Tree:
						if not tree_line_counted:
							tree_line_counted = True
							tree_line_count += 1
						tree_line_even = tree_line_count % 2 == 0
						x_pos_even = get_pos_x() % 2 == 0
						if (tree_line_even and x_pos_even) or (not tree_line_even and not x_pos_even):
							plant(entity)
						else:
							if (get_ground_type() == Grounds.Soil):
								till()
					else:
						if (get_ground_type() == Grounds.Grassland):
							till()
						plant(entity)
				else:
					if (get_ground_type() == Grounds.Soil):
						till()
				water.use_water()
				variables.random_fertilizer_func()
				if w < width - 1:
					move(horizontal_direction)
			if h < height - 1 and variables.use_turn_back:
				move(vertical_direction)
			elif not variables.use_turn_back:
				move(North)
			horizontal_direction = horizontal[horizontal_direction]
		if variables.use_turn_back:
			vertical_direction = vertical[vertical_direction]
		