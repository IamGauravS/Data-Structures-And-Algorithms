from trie_node import *


class Trie():
    def __init__(self):
        # Write your code here
        self.root = TrieNode()
        self.root.children = [None]*26
    
    # inserting string in trie
    def get_ordinal(self, ch):
        return ord(ch) - ord('a') 
    def insert(self, string):
        curr = self.root
        for ch in string:
            ord_i = self.get_ordinal(ch)
            if curr.children[ord_i] is None:
                new_node = TrieNode()
                new_node.children = [None]*26
                curr.children[ord_i] = new_node
            curr = curr.children[ord_i]
        curr.is_word = True
        
    
    # searching for a string
    def search(self, string):

        # Replace this placeholder return statement with your code
        
        curr = self.root 
        for ch in string:
            ord_i = self.get_ordinal(ch)
            if curr.children[ord_i] is not None:
                curr= curr.children[ord_i]
            else:
                return False 
        
        return curr.is_word 
            
    
    # searching for a prefix
    def search_prefix(self, prefix):

        # Replace this placeholder return statement with your code
        curr = self.root 
        for ch in prefix:
            ord_i = self.get_ordinal(ch)
            if curr.children[ord_i] is not None:
                curr= curr.children[ord_i]
            else:
                return False 
            
        return True 
