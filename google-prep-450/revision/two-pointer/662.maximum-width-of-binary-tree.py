#
# @lc app=leetcode id=662 lang=python3
#
# [662] Maximum Width of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        maxWidth = 0
        queue = deque([(root, 0)])

        while queue:
            queueLen = len(queue)
            maxW, minW = -float('inf'), float('inf')

            for i in range(queueLen):
                curr, width = queue.popleft()
                minW = min(minW, width)
                maxW = max(maxW, width)
                if curr.left:
                    queue.append((curr.left, 2*width+1))
                if curr.right:
                    queue.append((curr.right, 2*width+2))

            

            maxWidth = max(maxWidth, maxW-minW+1)


        return maxWidth 

        
# @lc code=end

