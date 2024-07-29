class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        height = len(board)
        width = len(board[0])
        
        visited = [[False for i in range(width)] for j in range(height)]
        
        stack = []
        
        ## add all the border areas in stack 
        
        for i in range(height):
            if board[i][0] == 'O' :
                stack.append((i, 0))
            if board[i][width-1] == 'O':
                stack.append((i, width-1))
                
        for j in range(width):
            if board[0][j] == 'O' :
                stack.append((0, j))
            if board[height-1][j] == 'O':
                stack.append((height-1, j))
                
                
        while stack:
            i, j = stack.pop()
            
            visited[i][j] = True 
            
            delta = [(0,1), (1,0), (0,-1), (-1,0)]
            
            for dx, dy in delta:
                newi = i+dx 
                newj = j+dy 
                
                if 0 <= newi < height and 0 <= newj <width and board[newi][newj] == 'O' and visited[newi][newj] == False:
                    stack.append((newi, newj))
                    
        for i in range(height):
            for j in range(width):
                if board[i][j] == 'O' and visited[i][j] == False:
                    board[i][j] = 'X'
                    
        return board
                    
        
            
            