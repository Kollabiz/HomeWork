src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def prev_gr(src):
	i = 0
	while i < len(src) - 1:
		prev = src[i]
		next = src[i + 1]
		if next:
			if next > prev:
				yield next
		i += 1


pg = prev_gr(src)
for i in pg:
	print(i, end = ' ')