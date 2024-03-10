class TrieNode():
  
  # Initialize TrieNode instance
  def __init__(self):
    # Empty list of child nodes
    self.children = []
    # False indicates this node is not the end of a word
    self.complete = False
    # Create 26 child nodes for each letter of alphabet
    for i in range(0, 26):
      self.children.append(None)

# Tip: You may use some of the code templates provided
# in the support files

class WordDictionary:
    def __init__(self):
        # Write your code
        self.root = TrieNode()

    def get_ordinal(self, ch):
        return ord(ch) - ord('a')
    
    def get_char_from_ordinal(self, number):
        return chr(number + ord('a'))
    
    def add_word(self, word):
        
        curr = self.root 
        for ch in word:
            ord_i = self.get_ordinal(ch)
            if curr.children[ord_i] == None:
                curr.children[ord_i] = TrieNode()
                
            curr= curr.children[ord_i]
            
        curr.complete = True
        
    def search_word_helper(self, word, curr, i):
        if i == len(word):
            return curr.complete
        
        if word[i] == '.':
            for ch in curr.children:
                if ch != None:
                    temp = self.search_word_helper(word, ch, i+1)
                    if temp == True:
                        return True 
            return False
        
        elif curr.children[self.get_ordinal(word[i])] != None:
            return self.search_word_helper(word, curr.children[self.get_ordinal(word[i])], i+1 )
        else:
            return False
                    

    def search_word(self, word):
        
        curr = self.root 
        return self.search_word_helper(word, curr, 0)

    def get_words_helper(self, curr, word, result):
        if curr == None:
            return 
        if curr.complete == True:
            result.append(word)
            
        for i in range(26):
            if curr.children[i] != None:
                ch = self.get_char_from_ordinal(i)
                self.get_words_helper(curr.children[i], word+ch, result)
                
        return 
                

    def get_words(self):
        # write your code here
        output = []
        self.get_words_helper(self.root, "", output)
        
        return output
            
        
        