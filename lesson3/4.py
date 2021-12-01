def thesaurus(names):
	fin = {}
	alpha = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
	for name in names:
		if not name[0].upper() in fin.keys():
			fin[name[0].upper()] = [name]
		else:
			fin[name[0].upper()].append(name)
	sorted_fin = {}
	for sym in alpha:
		if sym in fin.keys():
			sorted_fin[sym] = fin[sym]
	return sorted_fin

def thesaurus_adv(names):
	fin = {}
	alpha = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
	for sym in alpha:
		group = []
		for name in names:
			if name.split(' ')[1][0] == sym:
				group.append(name)
		if group:
			fin[sym] = thesaurus(group)
	
	return fin
