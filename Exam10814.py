N = int(input())

user_list = []
for i in range(N):
    line = input().split(' ')
    user_list.append(line)

def conquer(l1, l2):
    merged = []
    while(len(l1)>0 or len(l2)>0):
        if len(l1) == 0:
            merged.append(l2.pop(0))
            continue
        if len(l2) == 0:
            merged.append(l1.pop(0))
            continue

        if int(l1[0][0]) > int(l2[0][0]):
            merged.append(l2.pop(0))
        else:
            merged.append(l1.pop(0))

    return merged

def merge_sort(list, ):
    if len(list) == 1:
        return list

    pivot = int(len(list)/2)
    front = merge_sort(list[:pivot])
    back = merge_sort(list[pivot:])

    return conquer(front, back)

res = merge_sort(user_list)

for age, name in res:
    print(int(age), name)


