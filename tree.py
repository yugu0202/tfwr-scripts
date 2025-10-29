def plant_func(line, entity):
	y_pos_even = line % 2 == 0
	x_pos_even = get_pos_x() % 2 == 0
	if (y_pos_even and x_pos_even) or (not y_pos_even and not x_pos_even):
		plant(entity)
	else:
		if (get_ground_type() == Grounds.Soil):
			till()
	