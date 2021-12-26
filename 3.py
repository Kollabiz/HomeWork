tutors = [ 'Иван', 'Анастасия', 'Петр', 'Сергей', 
'Дмитрий', 'Борис', 'Елена', 'Евгения', 'Николай'] 
klasses = [ '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А' ]


def tutor_klass():
	for tutor, klass in zip(tutors, klasses):
		yield (tutor, klass)


tk = tutor_klass()
for pair in tk:
	print(pair)