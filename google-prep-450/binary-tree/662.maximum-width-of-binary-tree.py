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
        if not root:
            return 0

        queue = deque([(root, 0)])

        maxWidth = 0

        while queue:
            _, firstHeight = queue[0]
            queueLen = len(queue)

            for _ in range(queueLen):
                currNode , index = queue.popleft()
                index -= firstHeight

                if currNode.left:
                    queue.append((currNode.left, index * 2))
                if currNode.right:
                    queue.append((currNode.right, index * 2 + 1))

            maxWidth = max(maxWidth, index + 1)


        return maxWidth

        
# @lc code=end

