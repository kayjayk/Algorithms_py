import sys
T = int(sys.stdin.readline())
list_0 = [1, 0]
list_1 = [0, 1]

for i in range(2, 41):
    list_0.append(list_0[i-1] + list_0[i-2])
    list_1.append(list_1[i - 1] + list_1[i - 2])

for i in range(T):
    num = int(sys.stdin.readline())
    print(list_0[num], list_1[num])