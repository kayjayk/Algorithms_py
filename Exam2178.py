import sys
input = sys.stdin.readline
N, M = map(int, input().split())
maze = []
is_visited = [[False] * M for _ in range(N)]
for _ in range(N):
    line = list(map(int, list(input().rstrip())))
    maze.append(line)

def bfs():
    dist = 0
    queue = [[0, 0]]
    break_loop = False

    while len(queue) > 0:
        tmp_q = queue.copy()
        queue = []

        while len(tmp_q) > 0:
            visit_row, visit_col = tmp_q.pop(0)
            if is_visited[visit_row][visit_col] == False and maze[visit_row][visit_col] == 1:
                is_visited[visit_row][visit_col] = True

                if visit_row == N-1 and visit_col == M-1:
                    break_loop = True
                    break

                dir1 = [-1, 0, 1, 0]
                dir2 = [0, 1, 0, -1]
                for i in range(4):
                    next_row = visit_row + dir1[i]
                    next_col = visit_col + dir2[i]
                    if 0 <= next_row < N and 0 <= next_col < M and maze[next_row][next_col] == 1 and is_visited[next_row][next_col] == False:
                        queue.append([next_row, next_col])

        dist += 1
        if break_loop:
            break

    return dist

print(bfs())