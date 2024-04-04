def check_if_queen_attacking(board, i, j):
    n = len(board)

    # Check the column
    for row in range(i):
        if board[row][j] == 'Q':
            return True

    # Check upper left diagonal
    row, col = i - 1, j - 1
    while row >= 0 and col >= 0:
        if board[row][col] == 'Q':
            return True
        row -= 1
        col -= 1

    # Check upper right diagonal
    row, col = i - 1, j + 1
    while row >= 0 and col < n:
        if board[row][col] == 'Q':
            return True
        row -= 1
        col += 1

    return False


import copy

def canplace(board, i , no_of_queens, n, solutions):
    if no_of_queens == n:
        solutions.append(copy.deepcopy(board))
        return
    if i == n:
        return
    for j in range(n):
        if not check_if_queen_attacking(board, i, j):
            board[i][j] = 'Q'
            canplace(board, i+1, no_of_queens+1, n, solutions)
            board[i][j] = '.'  # reset the cell

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for i in range(n)] for j in range(n)]
        solutions = []
        canplace(board, 0, 0, n, solutions)
        return [[''.join(row) for row in solution] for solution in solutions]
    
    


