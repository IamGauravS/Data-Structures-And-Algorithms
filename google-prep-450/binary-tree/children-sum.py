class Solution:
    # Function to check whether all nodes of a tree have the value 
    # equal to the sum of their child nodes.
    def isSumProperty(self, root):
        # Base case: if root is None or it's a leaf node, return True (1)
        if root is None or (root.left is None and root.right is None):
            return 1
        
        leftValue = 0
        rightValue = 0
        
        # If left child exists, get its data
        if root.left:
            leftValue = root.left.data
            
        # If right child exists, get its data
        if root.right:
            rightValue = root.right.data
            
        # Check if the current node's data is equal to the sum of its children
        if root.data != leftValue + rightValue:
            return 0
        
        # Recursively check for left and right subtrees
        return self.isSumProperty(root.left) and self.isSumProperty(root.right)