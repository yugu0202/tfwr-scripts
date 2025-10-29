def harvest_func():
	harvest()

def plant_func(_line, entity):
	if (get_ground_type() == Grounds.Grassland):
		till()
	plant(entity)