import sys
from copy import deepcopy
N = int(sys.stdin.readline())
checker_board = []

def fill_blank(checker_board, row, col, N, col_list):
    result = deepcopy(checker_board)
    for i in range(row, N):
        result[i][col] = True
    for i in col_list:
        result[row][i] = True

    i, j = row, col
    while(0 <= i < N and 0 <= j < N):
        result[i][j] = True
        i += 1
        j += 1
    i, j = row, col
    while (0 <= i < N and 0 <= j < N):
        result[i][j] = True
        i += 1
        j -= 1

    return result

def put_on_queen(N, cnt, checker_board, col_list):
    if cnt == N:
        return True

    res = 0

    for i in range(cnt, N):
        if i>cnt:
            continue

        for j in col_list:
            if i == 0 and j >= int(N/2):
                continue
            if checker_board[i][j]:
                continue
            new_board = fill_blank(checker_board, i, j, N, col_list)
            col_copy = deepcopy(col_list)
            col_copy.remove(j)
            res += put_on_queen(N, cnt+1, new_board, col_copy)

    return res

cols = [i for i in range(N)]
print(put_on_queen(N, 0, checker_board, cols) * 2)