import heapq
import sys
input = sys.stdin.readline
N = int(input())
seq_pos = []
seq_neg = []

def operation(x):
    if x == 0:
        if len(seq_pos) == 0:
            if len(seq_neg) == 0:
                print(0)
            else:
                print(-heapq.heappop(seq_neg))
        else:
            if len(seq_neg) == 0:
                print(heapq.heappop(seq_pos))
            else:
                if seq_pos[0] >= seq_neg[0]:
                    print(-heapq.heappop(seq_neg))
                else:
                    print(heapq.heappop(seq_pos))
    else:
        if x < 0:
            heapq.heappush(seq_neg, -x)
        else:
            heapq.heappush(seq_pos, x)

for _ in range(N):
    operation(int(input()))