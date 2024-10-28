#
# @lc app=leetcode id=863 lang=python3
#
# [863] All Nodes Distance K in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict, deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        neighbors = defaultdict(list)
        

        stack = [root]
        while stack:
            currNode = stack.pop()

            if currNode.left:
                neighbors[currNode].append(currNode.left)
                neighbors[currNode.left].append(currNode)
                stack.append(currNode.left)

            if currNode.right:
                neighbors[currNode].append(currNode.right)
                neighbors[currNode.right].append(currNode)
                stack.append(currNode.right)

        result = []
        distance = 0
        queue = deque([(target, 0)])
        visited = set()
        visited.add(target)

        while queue:
            currNode, distance = queue.popleft()

            if distance == k:
                result.append(currNode.val)
                continue 

            
            for node in neighbors[currNode]:
                if node not in visited:
                    visited.add(node)
                    queue.append((node, distance+1))

        return result 
# @lc code=end

