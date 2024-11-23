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

        if p.val > q.val:
            p, q = q, p 

        while root:
            if root.val > q.val:  # both nodes are in leftside
                root = root.left 
            elif root.val < p.val:  # both nodes are in rightside 
                root = root.right 
            else:
                return root   ## both are on left and right side 

        return None  

        
# @lc code=end

