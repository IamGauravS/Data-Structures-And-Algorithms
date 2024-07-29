# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _isValidBst(self, root, lower, upper):
        if not root:
            return True 
        if root.val <= lower or root.val >= upper:
            return False
        isLeftValid = self._isValidBst(root.left, lower, root.val)
        isRightValid = self._isValidBst(root.right, root.val, upper)
        
        return isLeftValid and isRightValid
        
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._isValidBst(root, float('-inf'), float('inf'))
        
         