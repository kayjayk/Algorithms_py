import sys
N = int(sys.stdin.readline())
whole_paper = []
papers = [0, 0, 0]

for i in range(N):
    line = list(map(int, sys.stdin.readline().split(' ')))
    whole_paper.append(line)

def count_paper(start_row, start_col, length):
    if length == 1:
        papers[whole_paper[start_row][start_col] + 1] += 1
        return

    first = 0
    for i in range(start_row, start_row+length):
        for j in range(start_col, start_col+length):
            if i == start_row and j == start_col:
                first = whole_paper[i][j]
                continue
            else:
                if whole_paper[i][j] != first:
                    sub_len = int(length/3)
                    for k in range(start_row, start_row + length, sub_len):
                        for l in range(start_col, start_col + length, sub_len):
                            count_paper(k, l, sub_len)
                    return

    papers[first + 1] += 1

count_paper(0, 0, N)
print(papers[0])
print(papers[1])
print(papers[2])