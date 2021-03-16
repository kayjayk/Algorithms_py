import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
net = [[False] * N for _ in range(N)]
for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    net[v1-1][v2-1] = True
    net[v2 - 1][v1 - 1] = True

cnt = 0
is_visited = [False] * N

def dfs(V):
    global cnt

    if is_visited[V] == False:
        is_visited[V] = True
        if V != 0:
            cnt += 1

        for i in range(N):
            if net[i][V]:
                dfs(i)

dfs(0)
print(cnt)