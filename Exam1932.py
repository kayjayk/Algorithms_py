sizeOfTri = int(input())
listOfTri = list()

for i in range(sizeOfTri) :
    inputStr = input()
    inputStrListed = inputStr.split(" ")
    
    for j in range(len(inputStrListed)) :
        inputStrListed[j] = int(inputStrListed[j])
    
    listOfTri.append(inputStrListed)

for i in range(len(listOfTri) - 1, 0, -1) :
    for j in range(len(listOfTri[i]) - 1) :
        if listOfTri[i][j] >= listOfTri[i][j + 1] :
            listOfTri[i - 1][j] += listOfTri[i][j]
        else :
            listOfTri[i - 1][j] += listOfTri[i][j + 1]

print(listOfTri[0][0])