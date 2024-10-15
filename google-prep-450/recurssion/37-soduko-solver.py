class Solution:
    def checkIfSodukoPossible(self, board, currI, currJ, num):
        for i in range(9):
            # Check row
            if board[currI][i] == num:
                return False
            # Check column
            if board[i][currJ] == num:
                return False
            # Check 3x3 block
            blockRow = 3 * (currI // 3) + i // 3
            blockCol = 3 * (currJ // 3) + i % 3
            if board[blockRow][blockCol] == num:
                return False
        return True
    
    def solveSodukoHelper(self, board, currI, currJ):
        if currI == 9:
            return True 
        
        if currJ == 9:
            return self.solveSodukoHelper(board, currI + 1, 0)
        
        if board[currI][currJ] != '.':
            return self.solveSodukoHelper(board, currI, currJ + 1)
        
        for num in '123456789':
            if self.checkIfSodukoPossible(board, currI, currJ, num):
                board[currI][currJ] = num
                if self.solveSodukoHelper(board, currI, currJ + 1):
                    return True
                board[currI][currJ] = '.'

        return False 



    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solveSodukoHelper(board,0,0)



## more optimised

class Solution:
    def __init__(self):
        # To track numbers already in rows, columns, and 3x3 blocks
        self.rows = [set() for _ in range(9)]
        self.cols = [set() for _ in range(9)]
        self.blocks = [set() for _ in range(9)]

    def getBlockIndex(self, row, col):
        return (row // 3) * 3 + (col // 3)

    def solveSodukoHelper(self, board, currI, currJ):
        if currI == 9:  # Reached the end of the board
            return True
        
        if currJ == 9:  # Move to next row
            return self.solveSodukoHelper(board, currI + 1, 0)
        
        if board[currI][currJ] != '.':  # Skip already filled cells
            return self.solveSodukoHelper(board, currI, currJ + 1)

        blockIdx = self.getBlockIndex(currI, currJ)
        
        for num in '123456789':
            if num not in self.rows[currI] and num not in self.cols[currJ] and num not in self.blocks[blockIdx]:
                # Place the number and mark it in row, column, and block sets
                board[currI][currJ] = num
                self.rows[currI].add(num)
                self.cols[currJ].add(num)
                self.blocks[blockIdx].add(num)
                
                if self.solveSodukoHelper(board, currI, currJ + 1):
                    return True
                
                # Backtrack: remove the number
                board[currI][currJ] = '.'
                self.rows[currI].remove(num)
                self.cols[currJ].remove(num)
                self.blocks[blockIdx].remove(num)

        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Initialize sets for rows, columns, and blocks
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = board[i][j]
                    blockIdx = self.getBlockIndex(i, j)
                    self.rows[i].add(num)
                    self.cols[j].add(num)
                    self.blocks[blockIdx].add(num)
        
        self.solveSodukoHelper(board, 0, 0)
