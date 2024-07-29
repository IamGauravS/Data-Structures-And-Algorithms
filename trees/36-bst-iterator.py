class bst_iterator:
    def __init__(self, root):
        self.stack = []
        self.push_all(root)

    def push_all(self, node):
        
        while node:
            self.stack.append(curr)
            curr = curr.left 
            
    def has_next(self):
        return len(self.stack) > 0
    
    def next(self):
        if self.has_next:
            curr = self.pop()
            if curr.right:
                self.stack.append(curr.right)
                
            return curr.data 
        
        else:
            return None 