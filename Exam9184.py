import sys

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    elif a > 20 or b > 20 or c > 20:
        if res_list[20][20][20] != 0:
            return res_list[20][20][20]
        return w(20, 20, 20)

    elif a < b and b < c:
        res_tmp = [0, 0, 0]
        if res_list[a][b][c-1] != 0:
            res_tmp[0] = res_list[a][b][c-1]
        else:
            res_tmp[0] = w(a, b, c-1)
        if res_list[a][b-1][c-1] != 0:
            res_tmp[1] = res_list[a][b-1][c-1]
        else:
            res_tmp[1] = w(a, b-1, c-1)
        if res_list[a][b-1][c] != 0:
            res_tmp[2] = res_list[a][b-1][c]
        else:
            res_tmp[2] = w(a, b-1, c)
        return res_tmp[0] + res_tmp[1] - res_tmp[2]

    else:
        res_tmp = [0, 0, 0, 0]
        if res_list[a-1][b][c] != 0:
            res_tmp[0] = res_list[a-1][b][c]
        else:
            res_tmp[0] = w(a-1, b, c)
        if res_list[a-1][b - 1][c] != 0:
            res_tmp[1] = res_list[a-1][b - 1][c]
        else:
            res_tmp[1] = w(a-1, b-1, c)
        if res_list[a-1][b][c-1] != 0:
            res_tmp[2] = res_list[a-1][b][c-1]
        else:
            res_tmp[2] = w(a-1, b, c-1)
        if res_list[a-1][b-1][c-1] != 0:
            res_tmp[3] = res_list[a-1][b-1][c-1]
        else:
            res_tmp[3] = w(a-1, b-1, c-1)
        return res_tmp[0] + res_tmp[1] + res_tmp[2] - res_tmp[3]

res_list = [[[0] * 21 for i in range(21)] for j in range(21)]
res_list[0][0][0] = 1

while(True):
    a, b, c = map(int, sys.stdin.readline().split(' '))
    if a == -1 and b == -1 and c == -1:
        break

    print('w({}, {}, {}) = {}'.format(a, b, c, w(a, b, c)))