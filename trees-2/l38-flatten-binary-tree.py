# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        self.prev = None

        def flattenHelper(node):

            if node == None:
                return

            flattenHelper(node.right)
            flattenHelper(node.left)

            node.right = self.prev
            node.left = None

            self.prev = node


        flattenHelper(root)


        

