#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []
        
        queue = deque([root])
        reverse = False 
        result = []

        while queue:
            temp = []
            levelSize = len(queue)

            for i in range(levelSize):
                curr = queue.popleft()
                temp.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            if reverse:
                result.append(temp[::-1])
                reverse = False 
            else:
                result.append(temp)
                reverse = True

        return result 

            


# @lc code=end

