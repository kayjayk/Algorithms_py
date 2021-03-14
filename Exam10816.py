import sys
from collections import defaultdict
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split(' ')))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split(' ')))

res = []
num_dict = defaultdict(int)
for num in A:
    num_dict[num] += 1

for num in B:
    if num in num_dict.keys():
        res.append(str(num_dict[num]))
    else:
        res.append('0')

print(' '.join(res))