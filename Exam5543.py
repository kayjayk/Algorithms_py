import sys
burgers = []
beverages = []

burgers.append(int(sys.stdin.readline().strip()))
burgers.append(int(sys.stdin.readline().strip()))
burgers.append(int(sys.stdin.readline().strip()))
beverages.append(int(sys.stdin.readline().strip()))
beverages.append(int(sys.stdin.readline().strip()))

print(min(burgers) + min(beverages) - 50)