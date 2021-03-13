import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split(' ')))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split(' ')))

A.sort()

def binary_search(start, end, num_to_find):
    l = end - start
    if l == 1:
        if A[start] == num_to_find:
            return True
        else:
            return False

    else:
        pivot = int((end + start) / 2)
        if num_to_find >= A[pivot]:
            return binary_search(pivot, end, num_to_find)
        else:
            return binary_search(start, pivot, num_to_find)

for num in B:
    print(int(binary_search(0, N, num)))