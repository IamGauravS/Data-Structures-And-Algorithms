class Solution:
    def existHelper(self, curr_word, word, board, curri, currj, output, visited):
        if output[0] == True:
            return 
        
        if curr_word == word:
            output[0] = True 
            return
        
        if len(curr_word) > len(word):
            return 
        

    
        delta = [(0,1), (1,0), (0, -1), (-1, 0)]
        
        for dx, dy in delta:
            nexti  = curri+dx
            nextj = currj+dy
            if 0 <= nexti < len(board) and 0 <= nextj < len(board[0]) and (nexti,nextj) not in visited and word[len(curr_word)] == board[nexti][nextj]:
                visited.add((nexti, nextj))
                curr_word = curr_word + board[nexti][nextj]
                
                self.existHelper(curr_word, word, board, nexti, nextj, output, visited)
                
                visited.remove((nexti, nextj))
                curr_word = curr_word[:-1]
                
        return
                
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        if word == "":
            return True 
        
        
        output = [False]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    curri, currj = i,j
                    visited = set()
                    visited.add((curri, currj))
                    curr_word = board[curri][currj]
                    self.existHelper(curr_word, word, board, curri, currj, output, visited)
                    
                if output[0] == True:
                    return True 
        
        return False
    
    
    
## slight optimisation

class Solution:
    def existHelper(self, curr_word, word, board, curri, currj, visited):
        if curr_word == word:
            return True
        
        if len(curr_word) > len(word):
            return False

        delta = [(0,1), (1,0), (0, -1), (-1, 0)]
        
        for dx, dy in delta:
            nexti  = curri+dx
            nextj = currj+dy
            if 0 <= nexti < len(board) and 0 <= nextj < len(board[0]) and (nexti,nextj) not in visited and word[len(curr_word)] == board[nexti][nextj]:
                visited.add((nexti, nextj))
                curr_word += board[nexti][nextj]
                
                if self.existHelper(curr_word, word, board, nexti, nextj, visited):
                    return True
                
                visited.remove((nexti, nextj))
                curr_word = curr_word[:-1]
                
        return False
                
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        if word == "":
            return True 
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    curri, currj = i,j
                    visited = set()
                    visited.add((curri, currj))
                    curr_word = board[curri][currj]
                    if self.existHelper(curr_word, word, board, curri, currj, visited):
                        return True 
        
        return False