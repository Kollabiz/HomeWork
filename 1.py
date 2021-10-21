duration = 400153

seconds = duration % 60
minutes = (duration // 60) % 60
hours = (duration // (60 * 60)) % 24
days = duration // (60 * 60 * 24)

_time = [days, hours, minutes, seconds]
time = ''
names = [' дн ', ' час ', ' мин ', ' сек ']
for idx, value in enumerate(_time):
	if value > 0:
		time = time + str(value) + names[idx]

print(time)