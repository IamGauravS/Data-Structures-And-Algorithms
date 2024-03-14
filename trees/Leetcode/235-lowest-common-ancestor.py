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
        
        if root.val == p.val or root.val == q.val:
            return root 
        
        leftside = self.lowestCommonAncestor(root.left, p, q)
        rightside = self.lowestCommonAncestor(root.right, p, q)
        
        if leftside and rightside:
            return root 
        
        if leftside:
            return leftside
        if rightside:
            return rightside