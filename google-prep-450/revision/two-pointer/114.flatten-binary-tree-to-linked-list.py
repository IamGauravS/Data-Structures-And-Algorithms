#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
            global prev
            if node is None:
                return 

            flattenHelper(node.right)
            flattenHelper(node.left)

            node.right = self.prev
            node.left = None
            self.prev = node

            return 

        flattenHelper(root)
        return 
        
        
# @lc code=end

