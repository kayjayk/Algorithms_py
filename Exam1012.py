import sys
T = int(sys.stdin.readline())

def bfs(row, col):
    cabbage_cnt = 0
    queue = []
    if is_visited[row][col] == False and cabbage_map[row][col] == 1:
        queue.append([row, col])

    while(len(queue) > 0):
        visit_row, visit_col = queue.pop(0)
        if is_visited[visit_row][visit_col] == False and cabbage_map[visit_row][visit_col] == 1:
            is_visited[visit_row][visit_col] = True
            cabbage_cnt += 1
            dir1 = [-1, 0, 1, 0]
            dir2 = [0, -1, 0, 1]

            for i in range(4):
                next_row = visit_row + dir1[i]
                next_col = visit_col + dir2[i]
                if 0 <= next_row < N and 0 <= next_col < M:
                    queue.append([next_row, next_col])

    if cabbage_cnt > 0:
        return 1
    else:
        return 0

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    cabbage_map = [[0] * M for __ in range(N)]
    for __ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        cabbage_map[Y][X] = 1

    is_visited = [[False] * M for __ in range(N)]
    worm_cnt = 0

    for row in range(N):
        for col in range(M):
            worm_cnt += bfs(row, col)

    print(worm_cnt)