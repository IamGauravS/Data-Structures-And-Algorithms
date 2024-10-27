#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTreeHelper(self, root):
        if root is None:
            return 0
        
        lheight = self.diameterOfBinaryTreeHelper(root.left)
        rheight = self.diameterOfBinaryTreeHelper(root.right)

        self.diameter = max(self.diameter, lheight+rheight)

        return 1 + max(lheight, rheight)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameterOfBinaryTreeHelper(root)

        return self.diameter
        
# @lc code=end

