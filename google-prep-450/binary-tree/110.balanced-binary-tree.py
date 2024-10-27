#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalancedHelper(self, root):
        if root == None:
            return 0
        
        lheight = self.isBalancedHelper(root.left)
        rheight = self.isBalancedHelper(root.right)

        if lheight == -1 or rheight == -1:
            return -1

        if abs(lheight - rheight) > 1:
            return -1
        else:
            return 1 + max(lheight, rheight)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        if self.isBalancedHelper(root) == -1:
            return False 
        
        return True 
        
# @lc code=end

