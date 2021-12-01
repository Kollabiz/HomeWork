from random import choice

def get_jokes(n, repeat_words=True):
	# Списки со словами
	nouns = ["автомобиль", "лес", "огонь", "город", "дом"] 
	adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"] 
	adjectives = ["веселый", "яркий", "зеленый", "утопичный", 
"мягкий"]
	
	# Финальный список со всеми "шутками"
	jokes = []
	
	# Генерируем ровно n "шуток"
	while n:
		if not len(nouns) and not len(adverbs) and not len(adjectives):
			print('Out of words!')
			return(jokes)
		# Добавляем в наш список с "шутками" строку из трёх слов, выбранных функцией choice()
		noun = choice(nouns)
		adverb = choice(adverbs)
		adjective = choice(adjectives)
		jokes.append(f'{noun} {adverb} {adjective}')
		
		# Если мы установили, что функция не может повторяться, удаляем слова из списков чтобы их не повторять
		if not repeat_words:
			nouns.remove(noun)
			adverbs.remove(adverb)
			adjectives.remove(adjective)
		
		# Уменьшаем n, чтобы не зациклиться
		n -= 1
	
	return jokes
