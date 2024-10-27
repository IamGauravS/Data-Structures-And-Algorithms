#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        def preorderTraversalHelper(node):
            if node == None:
                return 
            
            output.append(node.val)
            preorderTraversalHelper(node.left)
            preorderTraversalHelper(node.right)

        preorderTraversalHelper(root)
        return output
        
# @lc code=end

## using stack

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []
        
        output = []
        stack = []

        stack.append(root)

        while stack:
            node = stack.pop()
            if node:
                output.append(node.val)
                
                ## push right child first so that left child is processed first
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)

        return output
