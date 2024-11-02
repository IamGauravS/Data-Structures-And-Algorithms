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
class NodeValue:
    def __init__(self, minNode, maxNode, Sum):
        self.maxNode = maxNode
        self.minNode = minNode
        self.Sum = Sum

class Solution:
    def largestBstHelper(self, node):
        if not node:
            return NodeValue(float('inf'), float('-inf'), 0)

        left = self.largestBstHelper(node.left)
        right = self.largestBstHelper(node.right)

        if left.maxNode < node.val and node.val < right.minNode:
            currSum=left.Sum+ right.Sum + node.val
            self.maxSum=max(self.maxSum,currSum)
            return NodeValue(min(node.val, left.minNode), max(node.val, right.maxNode),currSum)

        return NodeValue(float('-inf'), float('inf'), max(left.Sum, right.Sum))
    
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.maxSum=0
        ans=self.largestBstHelper(root).Sum 
        return self.maxSum
        
# @lc code=end

