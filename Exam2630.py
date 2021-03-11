import sys
N = int(sys.stdin.readline())
whole_square = []
papers = [0, 0]

for i in range(N):
    line = list(map(int, sys.stdin.readline().split(' ')))
    whole_square.append(line)

def count_paper(start_row, start_col, length):
    if length == 1:
        papers[whole_square[start_row][start_col]] += 1
        return

    first = 0
    for i in range(start_row, start_row+length):
        for j in range(start_col, start_col+length):
            if i == start_row and j == start_col:
                first = whole_square[i][j]
                continue
            else:
                if whole_square[i][j] != first:
                    count_paper(start_row, start_col, int(length/2))
                    count_paper(start_row + int(length/2), start_col, int(length/2))
                    count_paper(start_row, start_col + int(length/2), int(length/2))
                    count_paper(start_row + int(length/2), start_col + int(length/2), int(length/2))
                    return

    papers[first] += 1

count_paper(0, 0, N)

print(papers[0])
print(papers[1])