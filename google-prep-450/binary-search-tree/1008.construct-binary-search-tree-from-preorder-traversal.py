#
# @lc app=leetcode id=1008 lang=python3
#
# [1008] Construct Binary Search Tree from Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        idx = 0
        def helper(lower, upper):
            nonlocal idx 

            if idx == len(preorder) or preorder[idx] < lower or preorder[idx] > upper:
                return None 
            
            val = preorder[idx]
            idx += 1

            root = TreeNode(val)

            root.left = helper(lower, val)
            root.right = helper(val, upper)

            return root 
        
        return helper( -sys.maxsize, sys.maxsize)

# @lc code=end

