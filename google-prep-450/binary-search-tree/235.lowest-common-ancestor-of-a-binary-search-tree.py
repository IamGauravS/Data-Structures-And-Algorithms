#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
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
        if root is None:
            return None 
        
        while root:
            ## if both are small
            if p.val < root.val and q.val < root.val:
                root = root.left 

            ## if both are greater 
            elif p.val > root.val and q.val > root.val:
                root = root.right 
            
            else:
                return root 
            
        return None 
        
# @lc code=end

