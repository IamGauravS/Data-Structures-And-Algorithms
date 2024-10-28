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
    def lowestCommonAncestorHelper(self, root, p, q):
        if root is None:
            return None
        


        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestorHelper(root.left, p , q)
        right = self.lowestCommonAncestorHelper(root.right, p, q)

        if left and right:
            return root 
        
        return left if left else right 
        

        

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        return self.lowestCommonAncestorHelper(root, p, q)
# @lc code=end

