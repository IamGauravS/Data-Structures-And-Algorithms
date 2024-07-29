# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        left_range = -sys.maxsize -1
        right_range = sys.maxsize
        
        return self.isValidBSTHelper(root, left_range, right_range)
    
    
    def isValidBSTHelper(self, root, left_range, right_range):
        if root is None:
            return True 
        if root.val <= left_range or root.val >= right_range:
            return False
        
        
        
        left_check = self.isValidBSTHelper(root.left, left_range, root.val)
        right_check = self.isValidBSTHelper(root.right, root.val, right_range)
        
        return left_check and right_check