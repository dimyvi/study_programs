chess_board = [['.' for _ in range(8)] for _ in range(8)]
xy = input()
x, y = 'abcdefgh'.index(xy[0]), '87654321'.index(xy[1])
chess_board[y][x] = 'N'
for i in range(len(chess_board)):
    for j in range(len(chess_board)):
        if (x - i) ** 2 + (y - j) ** 2 == 5:
            chess_board[j][i] = '*'
for k in chess_board:
    print(*k)
