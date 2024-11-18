#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
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

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

