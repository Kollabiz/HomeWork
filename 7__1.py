def add_value(value):
    with open('bakery.txt', 'a') as bakery:
        bakery.write(str(value).ljust(10) + '\n')


def interface():
    working = True
    while working:
        value = input('Value to add to bakery log:\n>>> ')
        if value == 'exit':
            working = False
            break
        add_value(float(value))
        print(f'Added value {value} to bakery log')



interface()