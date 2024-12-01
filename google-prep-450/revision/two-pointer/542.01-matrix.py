#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i,j))
                if mat[i][j] == 1:
                    mat[i][j] = float('inf')

        delta = [(1,0), (-1,0), (0,1), (0,-1)]
        while queue:

            curri, currj = queue.popleft()

            for di, dj in delta:
                newi = curri + di
                newj = currj + dj

                while 0 <= newi < len(mat) and 0 <= newj < len(mat[0]) and mat[newi][newj] > 1 + mat[curri][currj]:
                    mat[newi][newj] = 1 + mat[curri][currj]
                    queue.append((newi, newj))

        return mat

        
# @lc code=end

