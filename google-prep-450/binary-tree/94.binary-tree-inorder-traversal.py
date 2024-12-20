#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        def inorderTraversalHelper(node):
            if node is None:
                return
            
            inorderTraversalHelper(node.left)
            output.append(node.val)
            inorderTraversalHelper(node.right)

        inorderTraversalHelper(root)
        return output
# @lc code=end

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        stack = []
        curr = root 

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left 

            curr = stack.pop()
            output.append(curr.val)
            curr = stack.right 


        return output