import sys
n = int(sys.stdin.readline())
seq = sorted(list(map(int, sys.stdin.readline().split())))
target = int(sys.stdin.readline())

cnt = 0
end = n - 1

for start in range(n):
    while(start < end):
        if seq[start] + seq[end] > target:
            end -= 1
        else:
            break
    if start == end:
        break
    if seq[start] + seq[end] == target:
        cnt += 1

print(cnt)