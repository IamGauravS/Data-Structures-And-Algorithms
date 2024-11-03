#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
from collections import deque
import sys 

from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        queue = deque()
        # Initialize distances for `0`s and set `1`s to infinity
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))  # Add all 0s to the queue
                else:
                    mat[r][c] = float('inf')  # Set `1`s to infinity

        # Direction vectors for exploring neighbors
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Perform BFS from all 0s
        while queue:
            r, c = queue.popleft()
            # Check all neighbors
            for dr, dc in delta:
                nr, nc = r + dr, c + dc
                # If the neighbor is in bounds and we found a shorter path
                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] > mat[r][c] + 1:
                    mat[nr][nc] = mat[r][c] + 1  # Update distance
                    queue.append((nr, nc))  # Add the updated cell to the queue

        return mat


# @lc code=end

