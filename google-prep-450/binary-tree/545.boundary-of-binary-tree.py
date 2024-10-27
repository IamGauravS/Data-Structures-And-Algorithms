#
# @lc app=leetcode id=545 lang=python3
#
# [545] Boundary of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrderTraversal(self, root, leafNodes):
        if root is None:
            return 
        
        # Traverse the left subtree
        self.inOrderTraversal(root.left, leafNodes)

        # Check if the current node is a leaf
        if not root.left and not root.right:
            leafNodes.append(root.val)

        # Traverse the right subtree
        self.inOrderTraversal(root.right, leafNodes)


    
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:

        boundary = [root.val] if root.left or root.right else []
        leftBoundry = []
        
        currNode = root.left 

        while currNode:
            if currNode.left or currNode.right:
                leftBoundry.append(currNode.val)

            if currNode.left:
                currNode = currNode.left 
            
            else :
                currNode = currNode.right

        leafNodes = []
        self.inOrderTraversal(root, leafNodes)

        rightBoundry = []

        currNode = root.right

        while currNode:
            if currNode.right or currNode.left:
                rightBoundry.append(currNode.val)
            
            if currNode.right:
                currNode = currNode.right 

            else:
                currNode = currNode.left 

        return boundary + leftBoundry + leafNodes + rightBoundry[::-1]

        
            

        
        
# @lc code=end

