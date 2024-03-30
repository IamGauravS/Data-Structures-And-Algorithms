# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDiameter(self, root, maxDiameter):
        if root is None:
            return 0
        lheight = self.findDiameter(root.left, maxDiameter)
        rheight = self.findDiameter(root.right, maxDiameter)
        maxDiameter[0] = max(maxDiameter[0],  lheight + rheight)
        
        return 1 + max(lheight, rheight)
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        maxDiameter = [-1]
        
        self.findDiameter(root, maxDiameter)
        
        return maxDiameter[0]