class Solution:
    def existHelper(self, curri, currj, wordIdx, word):
        if wordIdx == len(word):
            return True 
        if curri == len(self.board) and currj == len(self.board[0]):
            return False 
        
        moves = [(1,0), (0,-1), (-1, 0), (0, 1)]

        for move in moves:
            newI = curri + move[0]
            newJ = currj + move[1]

            if 0 <= newI < len(self.board) and 0 <= newJ < len(self.board[0]) and self.board[newI][newJ] == word[wordIdx] and (newI, newJ) not in self.visited:
                self.visited.add((newI, newJ))
                if self.existHelper(newI, newJ, wordIdx+1, word):
                    return True 
                self.visited.remove((newI, newJ))
                

        return False 




    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board

        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == word[0]:
                    self.visited = set()
                    self.visited.add((i,j))
                    if self.existHelper(i, j, 1, word):
                        return True 
                    
        return False 
