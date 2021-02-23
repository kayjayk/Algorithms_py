import sys

def w(a, b, c):

    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        if res_list[20][20][20] != 0:
            return res_list[20][20][20]
        return w(20, 20, 20)

    if res_list[a][b][c] != 0:
        return res_list[a][b][c]

    if a < b < c:
        res_list[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

    res_list[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return res_list[a][b][c]

res_list = [[[0] * 21 for i in range(21)] for j in range(21)]
res_list[0][0][0] = 1

while(True):
    a, b, c = map(int, sys.stdin.readline().split(' '))
    if a == -1 and b == -1 and c == -1:
        break

    print('w({}, {}, {}) = {}'.format(a, b, c, w(a, b, c)))