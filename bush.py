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
	start_pos_y = first_bush_line
	start_pos_x = (line - first_bush_line) * bush_workers
	for _i in range(line - start_pos_y):
		move(South)
	for _i in range(start_pos_x):
		move(East)
	
	for _i in range((bush_workers + 1) / 2 - 1):
		move(East)
		move(North)
	plant(Entities.Bush)
	while True:
		if can_harvest():
			cost = get_cost(Entities.Hedge)[Items.Weird_Substance]
			use_item(Items.Weird_Substance, cost * bush_workers)
			maze_runner.run()
	