# ランダムで肥料を撒く
def use_random_fertilizer():
	if random() <= 0.05 and num_items(Items.Fertilizer) >= 1:
		use_item(Items.Fertilizer)

def use_fertilizer():
	if not can_harvest() and num_items(Items.Fertilizer) >= 1:
		use_item(Items.Fertilizer)