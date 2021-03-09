import sys
N = int(sys.stdin.readline())
memo = [0 for i in range(N+1)]

memo[1] = 1
memo[0] = 1
for i in range(2, len(memo)):
    memo[i] = (memo[i-1] + memo[i-2]) % 15746

print(memo[N])