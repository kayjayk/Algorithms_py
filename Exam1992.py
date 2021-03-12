import sys
N = int(sys.stdin.readline())
whole_img = []
res = ''

for i in range(N):
    line = list(sys.stdin.readline())
    whole_img.append(line)

def compression(start_row, start_col, length):
    global res

    if length == 1:
        res += whole_img[start_row][start_col]
        return

    first = ''
    for i in range(start_row, start_row+length):
        for j in range(start_col, start_col+length):
            if i == start_row and j == start_col:
                first = whole_img[i][j]
                continue
            else:
                if whole_img[i][j] != first:
                    res += '('
                    compression(start_row, start_col, int(length/2))
                    compression(start_row, start_col + int(length / 2), int(length / 2))
                    compression(start_row + int(length/2), start_col, int(length/2))
                    compression(start_row + int(length/2), start_col + int(length/2), int(length/2))
                    res += ')'
                    return

    res += first

compression(0, 0, N)

print(res)