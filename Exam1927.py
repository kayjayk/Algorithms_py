import heapq
import sys
input = sys.stdin.readline
N = int(input())
seq = []

def operation(x):
    if x == 0:
        if len(seq) == 0:
            print(0)
        else:
            print(heapq.heappop(seq))
    else:
        heapq.heappush(seq, x)

for _ in range(N):
    operation(int(input()))