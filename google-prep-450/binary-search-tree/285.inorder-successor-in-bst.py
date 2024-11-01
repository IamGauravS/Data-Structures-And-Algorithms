#
# @lc app=leetcode id=285 lang=python3
#
# [285] Inorder Successor in BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        curr = root
        val = p.val
        ceil = None

        while curr:
            if val >= curr.val:
                curr = curr.right

            elif val < curr.val:
                ceil = curr
                curr = curr.left


        return ceil 
                

# @lc code=end

