# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return 
        
        stack = [root]
        
        while stack:
            curr_len = len(stack)
            for i in range(curr_len):
                curr = stack.pop()
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
                curr.left, curr.right = curr.right, curr.left 
                
                
        return root
                
                
### recursion

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root is None:
            return None 
        
        root.left , root.right = root.right, root.left 
        
        root.left  = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        
        return root 