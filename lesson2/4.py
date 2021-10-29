names = ['инженео-конструктор Игорь', 'Главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАЙ', 'директор аэлита']

greetings = []

for part in names:
    name = part.split(' ')[-1].capitalize()
    greetings.append(f'Привет, {name}!')

print('\n'.join(greetings))