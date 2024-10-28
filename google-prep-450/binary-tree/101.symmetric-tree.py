#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetricHelper(self, left, right):
        if left == None or right == None:
            return left == right 
        
        if left.val != right.val:
            return False 
        
        return self.isSymmetricHelper(left.left, right.right) and self.isSymmetricHelper(left.right, right.left)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True 
        return self.isSymmetricHelper(root.left, root.right)
# @lc code=end

