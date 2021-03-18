import sys
N = int(sys.stdin.readline())
liquids = sorted(list(map(int, sys.stdin.readline().split())))
summary = 10**9*2+1
liquid_value = [0, 0]

def binary_search(p1, start, end):
    if start > end:
        return

    global summary
    liquid1 = liquids[p1]
    pivot = int((start + end) / 2)

    liquid2 = liquids[pivot]
    liquid_sum = liquid1 + liquid2

    if abs(liquid_sum) < summary:
        summary = abs(liquid_sum)
        liquid_value[0] = liquid1
        liquid_value[1] = liquid2

    if liquid_sum < 0:
        binary_search(p1, pivot+1, end)
    else:
        binary_search(p1, start, pivot-1)

for p1 in range(N):
    binary_search(p1, p1+1, N-1)

print(liquid_value[0], liquid_value[1])