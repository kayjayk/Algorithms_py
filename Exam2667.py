import sys
N = int(sys.stdin.readline())
map = []
for _ in range(N):
    line = list(sys.stdin.readline().rstrip())
    for i in range(len(line)):
        line[i] = int(line[i])
    map.append(line)

is_visited = [[False] * N for _ in range(N)]
seg_cnt = []
row_dir = [-1, 0, 1, 0]
col_dir = [0, -1, 0, 1]

def dfs(row, col):
    global is_visited
    cnt = 0

    if not (0 <= row < N and 0 <= col < N):
        return 0

    if map[row][col] == 1 and not is_visited[row][col]:
        is_visited[row][col] = True
        cnt += 1

        for dir in range(4):
            cnt += dfs(row + row_dir[dir], col + col_dir[dir])

        return cnt
    else:
        return 0

for i in range(N):
    for j in range(N):
        house_cnt = dfs(i, j)
        if house_cnt > 0:
            seg_cnt.append(house_cnt)


seg_cnt.sort()
print(len(seg_cnt))
for cnt in seg_cnt:
    print(cnt)