import sys
N = int(sys.stdin.readline())

def check(row, col):
    if check_col[col]:
        return False
    if check_diag1[col-row+N-1]:
        return False
    if check_diag2[col+row]:
        return False
    return True

def dfs(row):
    if row == N:
        return True

    res = 0
    for col in range(N):
        if row == 0 and col >= N/2:
            continue
        if check(row, col):
            check_col[col] = True
            check_diag1[col - row + N - 1] = True
            check_diag2[col + row] = True
            res += dfs(row+1)
            check_col[col] = False
            check_diag1[col - row + N - 1] = False
            check_diag2[col + row] = False

    return res

check_col = [False] * N
check_diag1 = [False] * (2 * N - 1)
check_diag2 = [False] * (2 * N - 1)
print(dfs(0) * 2)