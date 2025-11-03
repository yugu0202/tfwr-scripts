def harvest_func():
	if get_entity_type() == Entities.Bush:
		cost = get_cost(Entities.Hedge)[Items.Weird_Substance]
		use_item(Items.Weird_Substance, cost)
	harvest()

def plant_func(_line, entity):
	plant(entity)
	
import variables
import maze_runner

def main(line, _e, _h, _p):
	first_bush_line = 0
	for v in variables.plant_rules:
		if v == Entities.Bush:
			break
		first_bush_line += variables.plant_rules[v]
	bush_workers = variables.plant_rules[Entities.Bush]
	center = ((bush_workers + 1) / 2 - 1)
	start_pos_y = first_bush_line + center
	start_pos_x = (line - first_bush_line) * bush_workers + center
	while True:
		diff_y = get_pos_y() - start_pos_y
		diff_x = get_pos_x() - start_pos_x
		if diff_y < 0:
			for _i in range(abs(diff_y)):
				move(North)
		else:
			for _i in range(diff_y):
				move(South)
		
		if diff_x < 0:
			for _i in range(abs(diff_x)):
				move(East)
		else:
			for _i in range(diff_x):
				move(West)
		
		plant(Entities.Bush)
		while True:
			if can_harvest():
				cost = get_cost(Entities.Hedge)[Items.Weird_Substance]
				use_item(Items.Weird_Substance, cost * bush_workers)
				maze_runner.run()
				break
	