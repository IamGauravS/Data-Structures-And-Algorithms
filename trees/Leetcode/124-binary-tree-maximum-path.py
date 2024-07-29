# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        maxi = [-sys.maxsize]
        self.maxPathSumHelper(root, maxi)
        
        return maxi[0]
    
    def maxPathSumHelper(self, root, maxi):
        if root is None:
            return 0 
        
        curr_val = root.val 
        right_val = max(0, self.maxPathSumHelper(root.right, maxi))
        left_val = max(0, self.maxPathSumHelper(root.left, maxi))
        
        if curr_val + right_val + left_val > maxi[0]:
            maxi[0] = curr_val + right_val + left_val
            
        return curr_val + max(left_val, right_val)
        
        