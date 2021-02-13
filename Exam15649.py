import sys
N, M = map(int, sys.stdin.readline().split(' '))

def print_num_list(num_list):
    res_str = ''
    for i in range(len(num_list)):
        res_str += str(num_list[i])
        if i < len(num_list) - 1:
            res_str += ' '

    print(res_str)

def sequence(N, M, cnt, num_list):
    if cnt == M:
        print_num_list(num_list)
    else:
        for i in range(1, N+1):
            if i in num_list:
                continue
            num_list.append(i)
            sequence(N, M, cnt+1, num_list)
            num_list.remove(i)

sequence(N, M, 0, list())

