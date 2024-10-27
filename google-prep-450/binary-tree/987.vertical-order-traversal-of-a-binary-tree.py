#
# @lc app=leetcode id=987 lang=python3
#
# [987] Vertical Order Traversal of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import List, Optional

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        # List to store (column, row, value) tuples
        node_list = []
        
        # BFS with column and row tracking
        queue = deque([(root, 0, 0)])  # (node, column, row)
        while queue:
            node, col, row = queue.popleft()
            if node:
                node_list.append((col, row, node.val))
                queue.append((node.left, col - 1, row + 1))
                queue.append((node.right, col + 1, row + 1))
        
        # Sort by column first, then row, then node value
        node_list.sort()

        # Organize the results by columns
        output = []
        last_column = float('-inf')
        for col, row, value in node_list:
            if col != last_column:
                output.append([])  # Start a new column
                last_column = col
            output[-1].append(value)
        
        return output


        



        

# @lc code=end

