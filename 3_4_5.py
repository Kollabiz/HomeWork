import os.path
from sys import exit
from json import dump


def get_hobbies():
    with open('users.txt', 'r', encoding='utf-8') as users, open('hobby.txt', 'r', encoding='utf-8') as hobbies:
        hobbies_dict = {}
        user, hobby = users.readline()[:-1], hobbies.readline()[:-1]
        while user:
            if not hobby:
                hobby = None
            hobbies_dict[user] = hobby
            user, hobby = users.readline(), hobbies.readline()
        if hobby:
            exit(1)
    with open('user_hobbies.txt', 'w', encoding='utf-8') as user_hobbies_file:
        dump(hobbies_dict, user_hobbies_file)


def merge_hobbies(infile1, infile2, outfile):
    with open(infile1, 'r', encoding='utf-8') as users, open(infile2, 'r', encoding='utf-8') as hobbies, open(outfile, 'a', encoding='utf-8') as f:
        user, hobby = users.readline(), hobbies.readline()
        while user:
            if not hobby:
                hobby = None
            user = user[:-1]
            f.write(f'{user}: {hobby}')
            user, hobby = users.readline(), hobbies.readline()
        if hobby:
            exit(1)


def interface():
    working = True
    while working:
        users = input('Usernames file name:\n>>> ')
        if users == 'exit':
            working = False
            exit()
        if not os.path.exists(users):
            print(f'File {users} Doesn`t exists!')
        hobbies = input('Hobbies file name:\n>>> ')
        if hobbies == 'exit':
            working = False
            exit()
        if not os.path.exists(hobbies):
            print(f'File {hobbies} Doesn`t exists!')
        outfile = input('Outfile file name:\n>>> ')
        if outfile == 'exit':
            working = False
            exit()
        merge_hobbies(users, hobbies, outfile)
        print(f'Users and hobbies were merged in {outfile} file')



interface()
