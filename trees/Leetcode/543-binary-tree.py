# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        maxi = [0]
        self.diameterofbinarytreehelper(root, maxi)
        return maxi[0]
    
    def diameterofbinarytreehelper(self, root, maxi):
        if root is None:
            return 0
        
        lh = self.diameterofbinarytreehelper(root.left, maxi)
        rh = self.diameterofbinarytreehelper(root.right, maxi)
        
        curr_height = 1 + lh + rh 
        if curr_height > maxi[0]:
            maxi[0] = curr_height
            
        return 1+ max(lh,rh)
    
        