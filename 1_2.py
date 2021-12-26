def odd_nums(n):
	for i in range(1, n + 1, 2):
		yield i


odd_to_15 = odd_nums(15)
print(next(odd_to_15))
print(next(odd_to_15))
n = 15
odd_to_15 = (i for i in range(1, n + 1, 2))
print(next(odd_to_15))
print(next(odd_to_15))