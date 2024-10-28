#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []
        
        result = []
        queue = deque([root])

        while queue:
            queueLen = len(queue)

            for _ in range(queueLen):
                currNode = queue.popleft()
                lastInLevel = currNode.val 

                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)

            result.append(lastInLevel)

        return result
        
# @lc code=end

