import sys
N, M = map(int, sys.stdin.readline().split(' '))

def sequence(N, M, cnt, num_list):
    if cnt == M:
        print(*num_list)
    else:
        if len(num_list) == 0:
            last_num = 1
        else:
            last_num = num_list[-1]
        for i in range(last_num, N+1):
            num_list.append(i)
            sequence(N, M, cnt+1, num_list)
            num_list.remove(i)

sequence(N, M, 0, list())

