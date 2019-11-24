n = int(input())
nlist = list()
for i in input().split():
    nlist.append(int(i))
nlist.sort()
print(nlist[0], nlist[n-1])