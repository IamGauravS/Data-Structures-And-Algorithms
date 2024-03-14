# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag = [True]
        
        self.balanced_binary_tree_helper(root, flag)
        return flag[0]
    
    
    def balanced_binary_tree_helper(self, root, flag):
        if root is None:
            return 0
        
        lh = self.balanced_binary_tree_helper(root.left, flag)
        rh = self.balanced_binary_tree_helper(root.right, flag)
        
        if abs(lh-rh) > 1:
            flag[0] = False
            
        return 1 + max(rh, lh)