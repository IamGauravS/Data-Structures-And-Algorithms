class TrieNode:
    def __init__(self):
        self.isWord = False 
        self.data = [None]*26

class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.count = 0

    def insert(self, word: str) -> None:
        currNode = self.root 
        for ch in word:
            ind = ord(ch) - 97
            if currNode.data[ind] == None:
                currNode.data[ind] = TrieNode()
            currNode = currNode.data[ind]
            if currNode.isWord == False:
                self.count += 1
                currNode.isWord = True 

    def search(self, word: str) -> bool:
        currNode = self.root 
        for ch in word:
            ind = ord(ch) - 97 
            if currNode.data[ind] == None:
                return False 
            currNode = currNode.data[ind]

        return currNode.isWord
        

    def startsWith(self, prefix: str) -> bool:

        currNode = self.root 
        for ch in prefix:
            ind = ord(ch) - 97
            if currNode.data[ind] == None:
                return False 
            currNode = currNode.data[ind]

        return True
def countDistinctSubstrings(s):
    trie = Trie()

    for i in range(len(s)):
        currWord = s[i:]
        trie.insert(currWord)

    return trie.count + 1
    
    # Write your code here