from collections import defaultdict
def isValidSudoku(board):
    board_set = defaultdict(set)
    col_set = defaultdict(set)
    row_set = defaultdict(set)

    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                box_row = i//3
                box_col = j//3
                box_corr = (box_row, box_col)
                if board[i][j] in row_set[i]:
                    return False
                if board[i][j] in col_set[j]:
                    return False
                if board[i][j] in board_set[box_corr]:
                    return False

                row_set[i].add(board[i][j])
                col_set[j].add(board[i][j])
                board_set[box_corr].add(board[i][j])

    return True

board = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

print(isValidSudoku(board))