def place_queens(board, queens):
    if queens == 0:
        return True

    for i in range(len(board)):
        for j in range(len(board[i])):
            if is_safe(board, i, j):
                board[i][j] = 1
                if place_queens(board, queens - 1):
                    return True
                board[i][j] = 0
    return False

def is_safe(board, row, col):
    for i in range(len(board[row])):
        if board[row][i] == 1:
            return False

    for i in range(len(board)):
        if board[i][col] == 1:
            return False

    i, j = row, col
    while i > 0 and j > 0:
        i -= 1
        j -= 1
        if board[i][j] == 1:
            return False

    i, j = row, col
    while i < len(board) - 1 and j > 0:
        i += 1
        j -= 1
        if board[i][j] == 1:
            return False

    i, j = row, col
    while i > 0 and j < len(board) - 1:
        i -= 1
        j += 1
        if board[i][j] == 1:
            return False

    i, j = row, col
    while i < len(board) - 1 and j < len(board) - 1:
        i += 1
        j += 1
        if board[i][j] == 1:
          return False
    return True

board = [[0 for _ in range(3)] for _ in range(3)] # _ is a throwaway variable
place_queens(board, 2)
for row in board:
    print(row)

