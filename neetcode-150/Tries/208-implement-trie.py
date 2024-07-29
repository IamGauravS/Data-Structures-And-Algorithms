class TrieNode:
    def __init__(self):
        self.is_word = False 
        self.data = [None]*26
        
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        currNode = self.root
        for ch in word:
            index = ord(ch) - 97
            if currNode.data[index] == None:
                currNode.data[index] = TrieNode()
            currNode = currNode.data[index]
            
        currNode.is_word = True
        return

    def search(self, word: str) -> bool:
        currNode = self.root 
        for ch in word:
            index = ord(ch) - 97
            if currNode.data[index] == None:
                return False 
            currNode = currNode.data[index]
            
        return currNode.is_word

    def startsWith(self, prefix: str) -> bool:
        currNode = self.root
        
        for ch in prefix:
            index = ord(ch) - 97
            if currNode.data[index] == None:
                return False 
            currNode = currNode.data[index]
            
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)