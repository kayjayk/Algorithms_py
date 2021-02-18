import sys
min_max = [1000000000, -1000000000]

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split(' ')))
operator_list = list(map(int, sys.stdin.readline().split(' ')))

def operation(operand, i, seq):
    if seq == 0:
        operand = num_list[0]
    res = 0
    if i == 0:
        res = operand + num_list[seq+1]
    elif i == 1:
        res = operand - num_list[seq+1]
    elif i == 2:
        res = operand * num_list[seq + 1]
    elif i == 3:
        if operand < 0:
            res = int((operand * (-1)) / num_list[seq+1]) * (-1)
        else:
            res = int(operand / num_list[seq + 1])

    return res

def dfs(operand, seq):
    if seq == N-1:
        if  operand > min_max[1]:
            min_max[1] = operand
        if operand < min_max[0]:
            min_max[0] = operand

    for i in range(4):
        if operator_list[i] > 0:
            operator_list[i] -= 1
            dfs(operation(operand, i, seq), seq+1)
            operator_list[i] += 1

dfs(0, 0)

print(min_max[1])
print(min_max[0])