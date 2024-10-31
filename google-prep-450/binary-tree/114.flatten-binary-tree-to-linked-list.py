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
class Solution:
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        prev = None 


        def flattenHelper(curr):
            nonlocal prev
            if curr == None:
                return 
            
            flattenHelper(curr.right)
            flattenHelper(curr.left)

            curr.right = prev 
            curr.left = None 
            prev = curr 

        flattenHelper(root)

        return 
        
# @lc code=end

def flatten(self, root):
    if not root:
        return 0
    
    stack = []

    stack.append(root)

    while stack:
        curr = stack.pop()
        if curr.right:
            stack.append(curr.right)

        if curr.left:
            stack.append(curr.left)

        if len(stack) > 0:
            curr.right = stack[-1]

        curr.left = None 

    
