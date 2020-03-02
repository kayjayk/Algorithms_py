n = 1
for i in range(3):
    n = n * int(input())

l = []
for i in range(10):
    l.append(0)

for i in range(len(str(n))):
    l[int(str(n)[i])] = l[int(str(n)[i])] + 1

for i in range(10):
    print(l[i])
