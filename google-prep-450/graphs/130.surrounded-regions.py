#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        queue = deque()
        visited = set()

        ## add all the corner "O" in the queue
        for r in range(len(board)):
            if board[r][0] == "O":
                queue.append((r, 0))
                visited.add((r, 0))
            if board[r][len(board[0]) -1] == "O":
                queue.append((r, len(board[0])-1))
                visited.add((r, len(board[0])-1))

        for c in range(1, len(board[0])):
            if board[0][c] == "O":
                queue.append((0, c))
                visited.add(((0, c)))
            if board[len(board) - 1][c] == "O":
                queue.append((len(board)-1, c))
                visited.add((len(board)-1, c))

        
        delta = [(1,0), (-1,0), (0,-1), (0,1)]
        while queue:
            curri, currj  = queue.popleft()
            for dx, dy in delta:
                newi = curri + dx 
                newj = currj + dy 

                if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                    if (newi, newj) not in visited and board[newi][newj] == "O":
                        queue.append((newi, newj))
                        visited.add((newi, newj))

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O' and (r, c) not in visited:
                    board[r][c] = 'X'

        return board
        
# @lc code=end

