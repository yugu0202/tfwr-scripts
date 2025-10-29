#要素がリストに含まれる場合にTrueを返します
def list_in(entity, list):
	for l in list:
		if (entity == l):
			return True
	return False

def dict_get(key, dict, default = None):
	if key in dict:
		return dict[key]
	return default

def measure_get(direction = None, default = 0):
	m = measure(direction)
	if m == None:
		return default
	return m

def init_pos():
	for i in range(get_pos_x()):
		move(West)
	
	for i in range(get_pos_y()):
		move(South)

# Entities: ライン数 の形式の辞書からライン数: Entitiesの辞書を作成する
def rule_to_plant_dict(rules):
	dict = {}
	line = 0
	for entity in rules:
		for _i in range(rules[entity]):
			dict[line] = entity
			line += 1
	return dict

	
# 関数を何も設定したくないときに使用します
def none_func(_1 = None, _2 = None, _3 = None):
	pass