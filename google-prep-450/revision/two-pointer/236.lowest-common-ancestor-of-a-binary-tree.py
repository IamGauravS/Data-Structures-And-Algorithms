#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root == None:
            return None 
        if root == p or root == q:
            return root 
        
        leftCheck = self.lowestCommonAncestor(root.left, p, q)
        rightCheck = self.lowestCommonAncestor(root.right, p, q)

        if leftCheck and rightCheck:
            return root 
        if leftCheck:
            return leftCheck
        else:
            return rightCheck
        
# @lc code=end

