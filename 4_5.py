import os


def get_upper_limit(num):
    if num == 0:
        return 10
    length_of_num = len(str(num))
    zeros = '0' * length_of_num
    limit = int(f'1{zeros}')
    return limit


def get_stats(dir):
    fls = {}
    fin_stat = {}
    max_key = 0
    for i in os.listdir(dir):
        folder = f'{dir}/{i}'
        if os.path.isfile(folder):
            st = os.stat(folder)
            size = get_upper_limit(st.st_size)
            if size not in fls.keys():
                fls[size] = (0, [i.split('.')[-1]])
            if i.split('.')[-1] not in fls[size][1]:
                fls[size][1].append(i.split('.')[-1])
            fls[size] = (fls[size][0] + 1, fls[size][1])
        elif os.path.isdir(folder):
            st_2 = get_stats(folder)
            for k, v in st_2.items():
                if k not in fls.keys():
                    fls[k] = (v[0], v[1])
                else:
                    fls[k] = (fls[k][0] + v[0], v[1])
    return fls


print(get_stats('my_project'))
