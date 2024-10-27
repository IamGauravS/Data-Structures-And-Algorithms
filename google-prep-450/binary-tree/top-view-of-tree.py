class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        
        if root is None:
            return []
            
        leftBoundry = []
        currNode = root.left 
        
        while currNode:
            leftBoundry.append(currNode.data)
            currNode = currNode.left
            
        rightBoundry = []
        currNode = root.right
        
        while currNode:
            rightBoundry.append(currNode.data)
            currNode = currNode.right
            
        return leftBoundry[::-1] + [root.data] + rightBoundry
        # code here