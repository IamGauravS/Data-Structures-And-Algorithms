class TrieNode:
    def __init__(self):
        self.is_word = False 
        self.data = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        currNode = self.root 
        for ch in word:
            if ch not in currNode.data:
                currNode.data[ch] = TrieNode() 
            currNode = currNode.data[ch]
            
        currNode.is_word = True
        return
    
    def _search(self, word, currNode, index):
        if index == len(word):
            return currNode.is_word
        
        currChar = word[index]
        if currChar == ".":
            for ch in currNode.data:
                if self._search(word, currNode.data[ch], index+1):
                    return True 
            
                
        elif currChar in currNode.data:
            return self._search(word, currNode.data[currChar], index+1)
        
        
        return False 
        
    
    def search(self, word: str) -> bool:
        return self._search(word, self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)