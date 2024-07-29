# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDiameter(self, root):
        if root is None:
            return 0

        lHeight = 0
        rHeight = 0

        if root.left:
            lHeight = self.findDiameter(root.left)

        if root.right:
            rHeight = self.findDiameter(root.right)

        self.diameter = max(self.diameter, lHeight + rHeight)

        return 1 + max(lHeight, rHeight)



    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        self.diameter = -float('inf')
        self.findDiameter(root) 

        return self.diameter