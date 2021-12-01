def num_translate_adv(num):
	is_capital = False
	if num[0].lower() != num[0]:
		is_capital = True
	
	translitions = {
		'zero': 'ноль',
		'one': 'один',
		'two': 'два',
		'three': 'три',
		'four': 'четыре',
		'five': 'пять',
		'six': 'шесть',
		'seven': 'семь',
		'eight': 'восемь',
		'nine': 'девять'
	}
	
	if num.lower() in translitions.keys():
		num_translated = translitions[num.lower()]
		if is_capital:
			num_translated = num_translated.capitalize()
		return num_translated

print(num_translate_adv('Nine'))
