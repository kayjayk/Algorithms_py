import sys
N, S = map(int, sys.stdin.readline().split())
seq = list(map(int, sys.stdin.readline().split()))

end = 0
summary = 0
min_len = N + 1

for start in range(N):
    while(summary < S and end < N):
        summary += seq[end]
        end += 1

    if min_len > (end - start) and summary >= S:
        min_len = end - start
    summary -= seq[start]

if min_len == N + 1:
    min_len = 0


print(min_len)