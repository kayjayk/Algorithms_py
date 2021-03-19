import sys
input = sys.stdin.readline
N = int(input())
deque = []
for _ in range(N):
    order = input().rstrip().split()
    if order[0] == "push_front":
        deque.insert(0, int(order[1]))
    elif order[0] == "push_back":
        deque.insert(len(deque), int(order[1]))
    elif order[0] == "pop_front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop(0))
    elif order[0] == "pop_back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop())
    elif order[0] == "size":
        print(len(deque))
    elif order[0] == "empty":
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == "front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif order[0] == "back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[len(deque) - 1])

