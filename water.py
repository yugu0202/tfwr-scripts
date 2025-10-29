#閾値がを下回った際に水やりを行います
def use_water(threshold = 0.5):
	if (get_water() <= threshold and num_items(Items.Water) >= 1):
		use_item(Items.Water)