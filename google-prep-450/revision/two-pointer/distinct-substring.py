class TrieNode:
    def __init__(self):
        self.data = [None]*26
        self.isWord = False 

class Trie:
    def __init__(self):
        self.root = TrieNode() 
        self.count = 0

    def insert(self, word):
        curr = self.root 

        for ch in word:
            ordCh = ord(ch) - ord('a')
            if curr.data[ordCh] == None:
                curr.data[ordCh] = TrieNode() 
                self.count += 1
            curr = curr.data[ordCh]

        curr.isWord = True 
        return 

def countDistinctSubstrings(s):
    # Write your code here

    trie = Trie()
    for i in range(len(s)):
        trie.insert(s[i:])

    return trie.count + 1