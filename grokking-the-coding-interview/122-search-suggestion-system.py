from trie_node import TrieNode


class Trie:
    def __init__(self):
        self.root = TrieNode()
        
        
    def insert(self, word):
        curr = self.root 
        
        for ch in word:
            if ch not in curr.children:
                new_node = TrieNode()
                curr.children[ch] = new_node
            curr = curr.children[ch]
            
            if len(curr.search_words) < 3:
                curr.search_words.append(word)
                
       
    def search(self, word):
        result = []
        node = self.root 
        for i, char in enumerate(word):
            if char not in node.children:
                temp = [[] for _ in range(len(word) - i)]
                return result + temp 
            else:
                node = node.children[char]
                result.append(node.search_words[:])
                
        return result
           
        
def suggested_products(products, search_word):

    # Replace this placeholder return statement with your code
    products.sort()
    trie = Trie()
    
    for p in products:
        trie.insert(p)
        
    return trie.search(search_word)
