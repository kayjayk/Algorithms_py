import sys
N = int(sys.stdin.readline())
checker_board = []

def put_on_queen(col):
    if col == N:
        return True
    res = 0

    for row in range(N):
        if col == 0 and row >= int(N/2):
            continue
        loc = (row, col)
        conflict = False
        for queen in checker_board:
            if queen[0] == loc[0] or abs(queen[0] - loc[0]) == abs(queen[1] - loc[1]):
                conflict = True
                break

        if not conflict:
            checker_board.append(loc)
            res += put_on_queen(col+1)
            checker_board.pop()

    return res
print(put_on_queen(0) * 2)