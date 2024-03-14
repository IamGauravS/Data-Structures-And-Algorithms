# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if len(preorder) == 0 or len(inorder) == 0:
            return None 
        
        root = TreeNode(preorder[0])
        
        idx = inorder.index(preorder[0])
        
        inorder_left  = inorder[:idx]
        inorder_right = inorder[idx+1:]
        
        preorder_left = preorder[1: len(inorder_left)+1]
        preorder_right = preorder[len(inorder_left) + 1: ]
        
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)
        
        return root 