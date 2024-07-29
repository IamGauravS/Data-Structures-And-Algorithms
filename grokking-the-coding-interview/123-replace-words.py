

class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
      
    def insert(self, word):
        curr = self.root 
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_word = True 
        
    def search_prefix(self, word):
        pre = ""
        curr = self.root 
        for ch in word:
            
            if ch in curr.children:
                pre = pre + ch 
                curr = curr.children[ch]
                if curr.is_word == True:
                    return pre 
            else:
                break
            
        return word
          
    
def replace_words(sentence, dictionary):

   # Replace this placeholder return statement with your code
   trie = Trie()
   for word in dictionary:
       trie.insert(word)
       
   sentence_list = sentence.split(" ")
   for i in range(len(sentence_list)):
       sentence_list[i] = trie.search_prefix(sentence_list[i])
       
   output = " ".join(sentence_list)
   return output
