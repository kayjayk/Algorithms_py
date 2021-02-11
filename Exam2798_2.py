N, M = map(int, input().split(' '))

number_list = list(map(int, input().split(' ')))

sum = 0
for i in range(len(number_list)-2):
    for j in range(i+1, len(number_list)-1):
        for k in range(j+1, len(number_list)):
            triple = number_list[i] + number_list[j] + number_list[k]
            if triple > sum and triple <= M:
                sum = triple

print(sum)