class Solution:
    
    def dfs(self, cell):
        i = cell[0]
        j = cell[1]
        
        self.visited[i][j] = True
        
        delta = [(0,1), (0,-1), (1,0), (-1,0)]
        for dx, dy in delta:
            nexti = i+dx 
            nextj = j+dy 
            if 0<= nexti < len(self.board) and 0 <= nextj < len(self.board[0]) and self.visited[nexti][nextj] == False and self.board[nexti][nextj] == 'O':
                self.dfs([nexti, nextj])
                
        return 
    
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.visited = [[False for i in range(len(self.board[0]))] for j in range(len(self.board))]
        
        borders = [[0, j] for j in range(len(self.board[0]))] + [[len(self.board) - 1, j] for j in range(len(self.board[0]))] + [[i, 0] for i in range(len(self.board))] + [[i, len(self.board[0]) - 1] for i in range(len(self.board))]
        
        for borderCell in borders:
            curri = borderCell[0]
            currj = borderCell[1]
            
            if self.board[curri][currj] == 'O' and self.visited[curri][currj] == False:
                self.dfs(borderCell)
                
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 'O' and self.visited[i][j] == False:
                    self.board[i][j] = 'X'
                    
        return self.board
            
            
## optimised 

class Solution:
    def dfs(self, i, j):
        if not (0 <= i < len(self.board)) or not (0 <= j < len(self.board[0])) or self.visited[i][j] or self.board[i][j] != 'O':
            return
        self.visited[i][j] = True
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            self.dfs(i + dx, j + dy)

    def solve(self, board: List[List[str]]) -> None:
        if not board: return
        self.board = board
        self.visited = [[False]*len(board[0]) for _ in range(len(board))]

        for i in range(len(board)):
            for j in [0, len(board[0])-1]:  ## this is a list not range
                if board[i][j] == 'O':
                    self.dfs(i, j)
        for i in [0, len(board)-1]:
            for j in range(len(board[0])):   ## same here
                if board[i][j] == 'O':
                    self.dfs(i, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and not self.visited[i][j]:
                    board[i][j] = 'X'