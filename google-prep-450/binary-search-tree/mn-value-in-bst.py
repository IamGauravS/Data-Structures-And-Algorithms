class Solution:
    #Function to find the minimum element in the given BST.
    def minValue(self, root):
        if root is None:
            return -1
        ##Your code here
        while root.left != None:
            root = root.left 
            
        return root.data