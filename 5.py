src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def filter_by_doubles(src):
	_src = src.copy()
	src_set = set(_src)
	i = 0
	while i < len(src):
		itm = src[i]
		if not itm in src_set:
			while itm in _src:
				_src.remove(itm)
		src_set.discard(itm)
		i += 1
	
	return _src


print(filter_by_doubles(src))