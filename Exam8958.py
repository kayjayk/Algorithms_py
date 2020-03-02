import math

def cal_point(quiz_result):
    point = 0
    res_list = quiz_result.split('X')
    for i in res_list:
        point += len(i)*(len(i)+1) / 2

    return int(point)

N = int(input())
for i in range(N):
    print(cal_point(input()))