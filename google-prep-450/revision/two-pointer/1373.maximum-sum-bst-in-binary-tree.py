#
# @lc app=leetcode id=1373 lang=python3
#
# [1373] Maximum Sum BST in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.

class NewNode:
    def __init__(self, currSum = 0, minValue = float('inf'), maxValue = -float('inf')):
        self.currSum = currSum
        self.minValue = minValue
        self.maxValue = maxValue

class Solution:
    def maxSumBsTHelper(self, root):
        if root == None:
            return NewNode()
        
        left = self.maxSumBsTHelper(root.left)
        right = self.maxSumBsTHelper(root.right)

        ## current node is greater than max of left and smaller than min of right
        if left.maxValue < root.val and right.minValue > root.val:
            currSum = left.currSum + root.val + right.currSum
            self.maxSum = max(self.maxSum, currSum)
            return NewNode(currSum = currSum, minValue = min(left.minValue, root.val), maxValue = max(right.maxValue, root.val))

        else:
            return NewNode(currSum = max(left.currSum, right.currSum), minValue = -float('inf'), maxValue = float('inf'))



    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.maxSum = 0
        output = self.maxSumBsTHelper(root)
        return self.maxSum
        
        
# @lc code=end

