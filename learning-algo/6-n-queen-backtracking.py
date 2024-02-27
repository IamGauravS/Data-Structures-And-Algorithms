
class solution:

    def issafe(self, row, col, board, n):
        duprow = row 
        dupcol = col 

        ## check diagonally
        while row>=0 and col>=0:
            if board[row][col] == 'Q':
                return False 
            row -=1
            col -=1

        col = dupcol
        row = duprow
        ## check same col 
        while col>=0:
            if board[row][col] == 'Q':
                return False 
            col -= 1

        row = duprow
        col = dupcol 
        while row < n and col >=0:
            if board[row][col] == 'Q':
                return False 
            row += 1
            col -= 1

        return True 

    def solve(self, col, board, ans, n):
        if col == n:
            ans.append(list(board))
        
        for row in range(n):  ### here we are trying at all the rows at a given column
            if self.issafe(row, col, board,n):  ## checks if it is safe to place a queen at that postion
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]   ## places the queen at that position 
                self.solve(col+1, board, ans,n)  ### if it works we will try all the rows at next given column
                board[row] = board[row][:col] + '.' + board[row][col+1:]


    def solvenqueens(self, n):
        ans = []
        board = ['.'*n for _ in range(n)]
        self.solve(0, board, ans, n)

        return ans 
    
