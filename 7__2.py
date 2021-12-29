from sys import argv


def show_log(startpoint, endpoint=None):
    extend_endpoint = False
    if endpoint is None:
        endpoint = 2
        extend_endpoint = True
    with open("bakery.txt", 'r') as log:
        i = 1
        while i < startpoint:
            log.readline()
            i += 1
        i = 0
        log_slice = []
        while i < endpoint:
            line = log.readline()
            log_slice.append(line[:-1])
            if extend_endpoint:
                endpoint += 1
            if not line:
                log_slice = log_slice[:-1]
                break
            i += 1
        return log_slice


def interface():
    if len(argv) == 2:
        print('\n'.join(show_log(int(argv[1]))))
    elif len(argv) == 3:
        print('\n'.join(show_log(int(argv[1]), int(argv[2]))[:-1]))
    elif len(argv) == 1:
        print('\n'.join(show_log(0)))


interface()
