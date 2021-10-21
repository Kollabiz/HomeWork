# part 0

cubes = []

for num in range(1, 1000):
	cubes.append(num ** 3)
	
# part a

sum = 0

for num in cubes:
	digit_sum = 0
	divider = 10
	while divider // 10 <= num:
		digit = num % divider // (divider // 10)
		digit_sum += digit
		divider *= 10
	if not digit_sum % 7:
		sum += num

print('Просто кубы: ' + str(sum))

# part c

idx = 0
while idx < len(cubes):
	cubes[idx] += 17
	idx += 1

sum = 0

for num in cubes:
	digit_sum = 0
	divider = 10
	while divider // 10 <= num:
		digit = num % divider // (divider // 10)
		digit_sum += digit
		divider *= 10
	if not digit_sum % 7:
		sum += num

print('Кубы + 17: ' + str(sum))