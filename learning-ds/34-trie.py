class TrieNode:
    def __init__(self, char=''):
        # Each node will hold a list of references to its child nodes
        self.children = [None] * 26  
        # Indicates whether this node marks the end of a word in the Trie
        self.is_end_word = False  
        # The character that this node represents
        self.char = char  

class Trie:
    def __init__(self):
        # The root node is an empty node and serves as the starting point of the Trie
        self.root = TrieNode()

    def get_index(self, t):
        # This function returns the ASCII value of the character minus the ASCII value of 'a'
        # This gives us a unique index for each lowercase letter
        return ord(t) - ord('a')
    
    def insert(self, key):
        # If the key is None, we return False
        if key is None:
            return False 
        
        # Convert the key into lowercase
        key = key.lower()
        # We start at the root node
        current = self.root  

        # For each letter in the key
        for letter in key:
            # We calculate the index for the letter
            index = self.get_index(letter) 
            # If the child node at the index is None, it means the letter does not exist yet
            # So we create a new TrieNode for this letter
            if current.children[index] == None:
                current.children[index] = TrieNode(letter)

            # We then move to the child node at the index
            current = current.children[index]

        # After we have inserted all the letters of the key, we mark the current node as the end of a word
        current.is_end_word = True

    def search(self, key):
        if key is None:
            return False 
        
        key = key.lower()
        current = self.root 
        
        for letter in key:
            index = self.get_index(letter)
            if current.children[index] != None:
                current = current.children[index]
            else:
                return False 
            
        if current == None:
            return False 
        if current.is_end_word == False:
            return False 
        return True 
    
    def isEmpty(self, root):
        for i in range(26):
            if root.children[i]:
                return False 
        return True 
    
    def remove(self, root, key, depth=0):
        if root == None:
            return None 
        
        if depth == len(key):
            if root.is_end_word:
                root.is_end_word = False 
            if self.isEmpty(root):
                root = None 
            return root 
        
        index = self.get_index(key[depth])
        root.children[index] = self.remove(root.children[index], key, depth+1)

        if self.isEmpty(root) and not root.is_end_word:
            root = None 
        return root
    
    def total_words_helper(self, node, count):
        if node is None:
            return 0
        if node.is_end_word:
            count += 1
        for child in node.children:
            if child is not None:
                count = self.total_words_helper(child, count)
        return count

    def total_words(self):
        count = 0
        count = self.total_words_helper(self.root, count)
        return count
    
    def find_words_helper(self, node, word, output_list):
        if node is None:
            return

        word += node.char
        if node.is_end_word:
            output_list.append(word)

        for child in node.children:
            if child is not None:
                self.find_words_helper(child, word, output_list)

        word = word[:-1]

    def find_words(self):
        output_list = []
        self.find_words_helper(self.root, "", output_list)
        return output_list
    
    output_list = []

def find_words_helper(root, word):
    global output_list
    if root is None:
        return ""

    word = word+root.char 
    if root.is_end_word:
        output_list.append(word)
    for child in root.children:
        if child is not None:
            find_words_helper(child, word)

    word = word[:-1]

    return word

    
    

def find_words(root):

    # Replace this placeholder return statement with your code
    global output_list
    find_words_helper(root, "")
    return output_list