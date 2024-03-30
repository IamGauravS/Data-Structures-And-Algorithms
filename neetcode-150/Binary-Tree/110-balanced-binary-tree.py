# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalancedHelper(self, root, isHeightBalanced):
        if root is None:
            return 0
        lheight = self.isBalancedHelper(root.left, isHeightBalanced)
        rheight = self.isBalancedHelper(root.right, isHeightBalanced)
        
        if abs(lheight - rheight) > 1:
            isHeightBalanced[0] =  False
        return 1 + max(lheight, rheight)
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True 
        isHeightBalanced = [True]
        
        self.isBalancedHelper(root, isHeightBalanced)
        return isHeightBalanced[0]