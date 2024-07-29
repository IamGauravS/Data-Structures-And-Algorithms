# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    def _maxPathSumHelper(self, root, maxPathSum):
        if root is None:
            return 0
        
        leftSum = self._maxPathSumHelper(root.left, maxPathSum)
        
        rightSum = self._maxPathSumHelper(root.right, maxPathSum)
            
        leftSum = leftSum if leftSum > 0 else 0
        rightSum = rightSum if rightSum > 0 else 0
        
        maxPathSum[0] = max( root.val + leftSum  + rightSum , maxPathSum[0])
        
        return root.val + max(leftSum, rightSum)
        
        
        
                
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        maxPathSum = [-sys.maxsize]
        
        self._maxPathSumHelper(root, maxPathSum) 
        
        return maxPathSum[0]