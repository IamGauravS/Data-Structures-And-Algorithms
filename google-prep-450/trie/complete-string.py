class TrieNode:
    def __init__(self):
        self.isWord = False 
        self.data = [None]*26

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        currNode = self.root 
        for ch in word:
            ind = ord(ch) - 97
            if currNode.data[ind] == None:
                currNode.data[ind] = TrieNode()
            currNode = currNode.data[ind]

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
    
    def isPerfect(self, word) -> bool:
        currNode = self.root 
        for ch in word:
            ind = ord(ch) - 97
            if currNode.data[ind].isWord == False:
                return False 
            currNode = currNode.data[ind]

        return True 
def completeString(n: int, a: List[str])-> str:
    
    trie = Trie()
    # Write your Code here
    for inpStr in a:
        trie.insert(inpStr)

    maxLen = 0
    outputStrs = []

    for inpStr in a:
        if trie.isPerfect(inpStr):
            if len(inpStr) > maxLen:
                outputStrs = []
                outputStrs.append(inpStr)
                maxLen = len(inpStr)

            elif len(inpStr) == maxLen:
                outputStrs.append(inpStr)
    if len(outputStrs) > 0:
        outputStrs.sort()
        return outputStrs[0]
    else:
        return None 