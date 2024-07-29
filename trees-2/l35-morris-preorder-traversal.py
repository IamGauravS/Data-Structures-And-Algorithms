# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root):
            if root == None:
                return 
            helper(root.left)
            inorder.append(root.val)
            helper(root.right)

            return

        inorder = []
        helper(root)
        return inorder