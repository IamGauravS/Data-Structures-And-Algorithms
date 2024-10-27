#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxPath = float('-inf')

    def maxPathSumHelper(self, root):
        if root is None:
            return 0
        
        lsum = max(0, self.maxPathSumHelper(root.left))
        rsum = max(0, self.maxPathSumHelper(root.right))

        self.maxPath = max(root.val + lsum + rsum, self.maxPath)

        return root.val + max(lsum, rsum)
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPathSumHelper(root)

        return self.maxPath
        
# @lc code=end

