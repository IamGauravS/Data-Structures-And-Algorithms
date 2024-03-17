
def check_if_valid_soduko(board, i, j, number):
    # Check the row
    number = str(number)
    for x in range(9):
        if board[i][x] == number:
            return False

    # Check the column
    for x in range(9):
        if board[x][j] == number:
            return False

    # Check the box
    startRow = i - i % 3
    startCol = j - j % 3
    for x in range(3):
        for y in range(3):
            if board[x + startRow][y + startCol] == number:
                return False

    return True



def soduko_solver_helper(board, i, j, output):
    if i == 9 :
        output.append(board)
        return 
    
    if i == 9:
        soduko_solver_helper(board, 0, j+1, output)
        return 
    
    if board[i][j] != '.':
        soduko_solver_helper(board, i+1, j, output)
        return 
    
    
    for num in range(1, 10):
        if check_if_valid_soduko(board, i, j, num):
            board[i][j] = num
            soduko_solver_helper(board, i+1, j, output)
            board[i][j] = '.'
            
    return 
            


def soduko_solver(board):
    ## board can have some number already filled
    output = []
    soduko_solver_helper(board, 0 , 0, output)
    return output