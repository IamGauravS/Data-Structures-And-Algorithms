from backtracking import *

# Tip: You may use some of the code templates provided
# in the support files
def is_queen_attacked_diagonally(board, x, y):
    # Check left diagonals
    for i in range(len(board)):
        if board[i][y] == 1:
            return True 
        
    i, j = x - 1, y - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return True
        i -= 1
        j -= 1

    i, j = x + 1, y + 1
    while i < 8 and j < 8:
        if board[i][j] == 1:
            return True
        i += 1
        j += 1

    # Check right diagonals
    i, j = x - 1, y + 1
    while i >= 0 and j < 8:
        if board[i][j] == 1:
            return True
        i -= 1
        j += 1

    i, j = x + 1, y - 1
    while i < 8 and j >= 0:
        if board[i][j] == 1:
            return True
        i += 1
        j -= 1

    return False

def solve_n_queens_helper(grid, no_of_queens, n, current_row, total_ways):
    
    if no_of_queens == n:
        return 1 
    if current_row == n:
        return 0
    
    for i in range(n):
        ## place it on different position on row
        grid[current_row][i] = 1
        if is_queen_attacked_diagonally(grid, current_row, i) == False:
            possible = solve_n_queens_helper(grid, no_of_queens+1, n, current_row+1)
            total_ways = total_ways+ possible
        grid[current_row][n] = 0
        
        
    return total_ways
    

def solve_n_queens(n):

    # Replace this placeholder return statement with your code
    no_of_solutions = 0
    grid = [[o for i in range(n)] for j in range(n)]
    
       
    no_of_solutions = solve_n_queens_helper(grid, 0, n, 0, 0)
    return no_of_solutions