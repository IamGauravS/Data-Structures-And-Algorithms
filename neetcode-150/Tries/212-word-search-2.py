
class TrieNode:
    def __init__(self):
        self.is_word = False 
        self.data = {}
        self.word = ""
        

class Solution:
    def insert(self, word, currNode) -> None:
        
        for ch in word:
            if ch not in currNode.data:
                currNode.data[ch] = TrieNode() 
            currNode = currNode.data[ch]
            
        currNode.is_word = True
        currNode.word = word
        return
    
    def _findWordsHelper(self, curri, currj, currNode, visited):
        currBoardChar = self.board[curri][currj]
        
        if currBoardChar not in currNode.data:
            return
         
        if currNode.data[currBoardChar].is_word == True:
            self.output.append(currNode.data[currBoardChar].word)
            
        
        currNode = currNode.data[currBoardChar]
            
        delta = [(1,0), (-1,0), (0,1), (0,-1)]
        
        for dx, dy in delta:
            nexti = curri+dx 
            nextj = currj+dy
            if 0 <= nexti < len(self.board) and 0 <= nextj < len(self.board[0]) and (nexti, nextj) not in visited and self.board[nexti][nextj] in currNode.data:
                visited.add((nexti, nextj))
                self._findWordsHelper(nexti, nextj, currNode, visited)
                visited.remove((nexti, nextj))
                
        return 
        
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.output = []
        self.board = board
        t  = TrieNode()
        
        
        for word in words:
            self.insert(word, t)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = set()
                visited.add((i,j))
                self._findWordsHelper(i, j, t, visited)
                
        return list(set(self.output))
        