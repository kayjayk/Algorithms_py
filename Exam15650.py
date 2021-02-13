import sys
N, M = map(int, sys.stdin.readline().split(' '))

def print_num_list(num_list):
    res_str = ''
    for i in range(len(num_list)):
        res_str += str(num_list[i])
        if i < len(num_list) - 1:
            res_str += ' '

    print(res_str)

def permutation(N, M, cnt, num_list):
    if cnt == M:
        print_num_list(num_list)
    else:
        if len(num_list) == 0:
            last_num = 0
        else:
            last_num = num_list[-1]
        for i in range(last_num+1, N+1):
            num_list.append(i)
            permutation(N, M, cnt+1, num_list)
            num_list.remove(i)

permutation(N, M, 0, list())

