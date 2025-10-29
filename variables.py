import util
import fertilizer

# General

plant_rules = {
	Entities.Tree: 4,
	Entities.Carrot: 5,
	Entities.Pumpkin: 6,
	Entities.Sunflower: 4,
	Entities.Cactus: 4,
	Entities.Bush: 5,
}

water_threshold = 0.6
use_turn_back = False
random_fertilizer_func = fertilizer.use_random_fertilizer

# harvest

parallel_horizontal_harvest = 32
parallel_vertical_harvest = 1

# line_farmer

parallel_vertical_farmer = 32