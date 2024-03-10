class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_word = False
        

class Trie:
    def __init__(self):
        self.root = TrieNode()
      
    def insert(self, number):
        word = str(number)
        curr = self.root 
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_word = True 
        
    def get_all_words(self):
        result = []
        self.dfs(self.root, '', result)
        return result

    def dfs(self, node, word, result):
        if node.is_word:
            result.append(word)
        for ch, child in node.children.items():
            self.dfs(child, word + ch, result)
        


def lexicographical_order(n):
    trie = Trie()
    for i in range(1, n+1):
        trie.insert(i)
        
    output = [int(word) for word in trie.get_all_words()]
    return output