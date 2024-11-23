#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBSTHelper(self, root, minLeft, maxRight):
        if root is None:
            return True 
        
        if root.val <= minLeft or root.val >= maxRight:
            return False 
        else:
            return self.isValidBSTHelper(root.left, minLeft, root.val) and self.isValidBSTHelper(root.right, root.val, maxRight)
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTHelper(root, -float('inf'), float('inf'))
        
# @lc code=end

