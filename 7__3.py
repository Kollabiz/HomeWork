def edit_log(no, val):
    with open('bakery.txt', 'r+', encoding='utf-8') as log:
        log.seek(11 * no + 1)
        log.write(str(val).ljust(10) + '\n')


def interface():
    working = True
    while working:
        no = input('Number of record to edit (int):\n>>> ')
        if no == 'exit':
            working = False
            break
        val = input('Value to change the existing one (float):\n>>> ')
        if val == 'exit':
            working = False
            break
        no = int(no)
        val = float(val)
        edit_log(no, val)



interface()
