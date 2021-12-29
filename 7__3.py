def edit_log(no, val):
    with open('bakery.txt', 'r+', encoding='utf-8') as log:
        log.seek(11 * no + 1)
        log.write(str(val).ljust(10) + '\n')


def interface():
    no = int(input('Number of record to edit (int):\n>>> '))
    val = float(input('Value to change the existing one (float):\n>>> '))
    ans = edit_log(no, val)
    if ans:
        print(ans)


while True:
    interface()
