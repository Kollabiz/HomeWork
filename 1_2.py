def parse_requests_log(log):
    with open(log, 'r') as r_log:
        log_list = []
        for line in r_log:
            addr, _, _, date0, date1, request_type, path = line.split(' ')[:7]
            block = (addr, request_type[1:], path)
            log_list.append(block)
        return log_list


def recognize_spammer(log):
    potential_spammer = '0.0.0.0'
    request_counts = {
        '0.0.0.0': 0
    }
    for request in log:
        ip = request[0]
        if not ip in request_counts.keys():
            request_counts[ip] = 0
        request_counts[ip] += 1
        if request_counts[potential_spammer] < request_counts[ip]:
            potential_spammer = ip

    return potential_spammer


log = parse_requests_log('requests.txt')
spammer = recognize_spammer(log)
print(spammer)
