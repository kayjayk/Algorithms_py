N = int(input())
grades = input().split()

for i in range(len(grades)):
    grades[i] = int(grades[i])

highest = max(grades)
print(sum(grades) / len(grades) / highest * 100)