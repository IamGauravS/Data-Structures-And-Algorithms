# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSumHelper(self, root):
        if root is None:
            return 0

        leftSum = -float('inf')
        rightSum = -float('inf')

        if root.left:
            leftSum = self.maxPathSumHelper(root.left)

        if root.right:
            rightSum = self.maxPathSumHelper(root.right)

        leftSum = leftSum if leftSum > 0 else 0
        rightSum = rightSum if rightSum > 0 else 0


        self.maxSum = max(self.maxSum, root.val + leftSum +  rightSum)

        return root.val + max(leftSum, rightSum)
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        self.maxSum = -float('inf')

        self.maxPathSumHelper(root)

        return self.maxSum