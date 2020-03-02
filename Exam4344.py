import sys
C = int(input())

for i in range(C):
    tmp = sys.stdin.readline().split(" ")
    N = int(tmp[0])
    tmp.pop(0)

    for i in range(N):
        tmp[i] = int(tmp[i])

    avg = sum(tmp) / len(tmp)
    cnt = 0

    for i in range(N):
        if tmp[i] > avg:
            cnt += 1

    print("%.3f%%" % (cnt/len(tmp)*100))