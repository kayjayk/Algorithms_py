import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split(' '))
    queue = list(map(int, sys.stdin.readline().split(' ')))
    cnt = 0

    while(True):
        max_num = max(queue)

        if queue[0] == max_num:
            queue.pop(0)
            cnt += 1
            if M == 0:
                break
            else:
                M -= 1

        else:
            tmp = queue.pop(0)
            queue.append(tmp)
            if M == 0:
                M = len(queue) - 1
            else:
                M -= 1

    print(cnt)