class Solution:
    def floor(self, root, x):
        # Code here
        if root is None:
            return -1
            
        floor = -1
        while root:
            if root.data == x:
                return root.data
                
            if x < root.data:
                root = root.left
            else :
                floor = root.data
                root = root.right 
                
                
        return floor