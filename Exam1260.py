import sys
N, M, V = map(int, sys.stdin.readline().split())
graph = [[False] * N for _ in range(N)]
for _ in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1-1][n2-1] = True
    graph[n2-1][n1-1] = True


dfs_seq = []
bfs_seq = []
dfs_visited = [False] * N
bfs_visited = [False] * N

def dfs(V):
    if dfs_visited[V] == False:
        dfs_visited[V] = True
        dfs_seq.append(str(V+1))
    else:
        return

    for i in range(N):
        if i == V:
            continue
        if graph[V][i]:
            dfs(i)

def bfs(V):
    queue = [V]

    while(len(queue) > 0):
        node = queue.pop(0)

        if bfs_visited[node] == False:
            bfs_visited[node] = True
            bfs_seq.append(str(node + 1))

            for i in range(N):
                if i == node:
                    continue
                if graph[node][i]:
                    queue.append(i)

dfs(V-1)
bfs(V-1)

print(' '.join(dfs_seq))
print(' '.join(bfs_seq))
