#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        def postorderTraversalHelper(node):
            if node == None:
                return 
            
            postorderTraversalHelper(node.left)
            postorderTraversalHelper(node.right)
            output.append(node.val)

        postorderTraversalHelper(root)
        return output
        
# @lc code=end

