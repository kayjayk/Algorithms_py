import sys
N, M = map(int, sys.stdin.readline().split(' '))

def sequence(N, M, cnt, num_list):
    if cnt == M:
        print(*num_list)
    else:
        for i in range(1, N+1):
            num_list.append(i)
            sequence(N, M, cnt+1, num_list)
            num_list.pop()

sequence(N, M, 0, list())

