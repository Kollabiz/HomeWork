def add_value(value):
    with open('bakery.txt', 'a') as bakery:
        bakery.write(str(value).ljust(10) + '\n')


def interface():
    value = float(input('Value to add to bakery log:\n>>> '))
    add_value(value)
    print(f'Added value {value} to bakery log')


while True:
    interface()