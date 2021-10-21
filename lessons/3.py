words = [' процент', ' процента', ' процентов']

for precent in range(1, 100):
	if precent > 19 or precent < 10:
		if precent % 10 == 1:
			print(str(precent) + words[0])
		elif precent % 10 < 5 and precent % 10 != 0:
			print(str(precent) + words[1])
		elif precent % 10 >= 5 or precent % 10 == 0:
			print(str(precent) + words[2])
	else:
		print(str(precent) + words[2])