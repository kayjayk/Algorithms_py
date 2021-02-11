N, M = map(int, input().split(' '))

max_to_color = 8*8;
min_to_color = 8*8/2;
original_board = []
for i in range(N):
    line = input()
    original_board.append(list(line))

for i in range(N-7):
    for j in range(M-7):
        cnt = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l)%2 == 0:
                    if original_board[k][l] == 'W':
                        cnt += 1
                    else:
                        pass
                else:
                    if original_board[k][l] == 'B':
                        cnt += 1
                    else:
                        pass

        if cnt > max_to_color/2:
            cnt = max_to_color - cnt

        if cnt < min_to_color:
            min_to_color = cnt

print(int(min_to_color))

