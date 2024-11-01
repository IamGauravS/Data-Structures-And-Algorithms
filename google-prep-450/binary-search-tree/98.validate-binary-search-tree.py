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
import sys 
class Solution:
    def isValidBSTHelper(self, root, maxValue, minValue):
        if root is None:
            return True 
        
        if root.val >= maxValue or root.val <= minValue:
            return False 
        
        return self.isValidBSTHelper(root.left, root.val, minValue) and self.isValidBSTHelper(root.right, maxValue, root.val)


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        maxValue = sys.maxsize
        minValue = -sys.maxsize

        return self.isValidBSTHelper(root, maxValue, minValue) 

# @lc code=end

