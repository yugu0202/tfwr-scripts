import variables
import util
import harvest
import dinasor

change_hat(Hats.Brown_Hat)

util.init_pos()

h = get_world_size() / variables.parallel_vertical_harvest // 1
w = get_world_size() / variables.parallel_horizontal_harvest // 1

for i in range(variables.parallel_vertical_harvest):
	for y in range(h * i - get_pos_y()):
		move(North)
	for back in range(get_pos_x()):
		move(West)
	for v in range(variables.parallel_horizontal_harvest):
		for x in range(w * v - get_pos_x()):
			move(East)
		if spawn_drone(harvest.main) == None:
			harvest.main()

for x in range(w):
	move(East)

dinasor.dinasor()