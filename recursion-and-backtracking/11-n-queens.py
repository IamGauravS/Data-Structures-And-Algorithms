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


def canplace(board, i , no_of_queens, n):
    if no_of_queens == n:
        return 1 
    if i == n:
        return 0
    total_no_of_ways = 0
    for j in range(n):
        if not check_if_queen_attacking(board, i, j):
            board[i][j] = 'Q'
            total_no_of_ways += canplace(board, i+1, no_of_queens+1, n)
            board[i][j] = 0 
    
    return total_no_of_ways

def n_queens(n):
    board = [[0 for i in range(n)] for j in range(n)]
    
    return canplace(board, 0, 0, n)
    
    


