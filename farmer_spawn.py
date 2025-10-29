import variables
import util
import line_farmer

import general_entity
import bush
import tree
import cactus

change_hat(Hats.Brown_Hat)

clear()
plant_dict = util.rule_to_plant_dict(variables.plant_rules)

h = get_world_size() / variables.parallel_vertical_farmer // 1

for v in range(variables.parallel_vertical_farmer):
	for x in range(h * v - get_pos_y()):
		move(North)
	y_pos = get_pos_y()
	entity = util.dict_get(y_pos, plant_dict)
	fmain = line_farmer.main
	harvest_func = None
	plant_func = None
	if entity == None:
		# =藁だった場合
		plant_func = util.none_func
	if entity == Entities.Bush:
		fmain = bush.main
	elif entity == Entities.Tree:
		plant_func = tree.plant_func
	
	if str(harvest_func) == "None":
		harvest_func = general_entity.harvest_func
	if str(plant_func) == "None":
		plant_func = general_entity.plant_func
	
	def farmer_main():
		fmain(y_pos, entity, harvest_func, plant_func)
	if spawn_drone(farmer_main) == None:
		farmer_main()

for x in range(w):
	move(East)

dinasor.dinasor()