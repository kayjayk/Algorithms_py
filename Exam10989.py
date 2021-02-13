import sys
from collections import defaultdict

N = int(sys.stdin.readline())
num_dict = defaultdict(int)

for i in range(N):
    num_dict[int(sys.stdin.readline())] += 1

num_keys = []
for key in num_dict.keys():
    num_keys.append(key)

sorted_keys = sorted(num_keys)

for i in range(len(sorted_keys)):
    key = sorted_keys[i]
    for j in range(num_dict[key]):
        print(key)