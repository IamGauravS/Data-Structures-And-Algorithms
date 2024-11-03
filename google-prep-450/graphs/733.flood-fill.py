#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start

from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue = deque()
        queue.append((sr,sc))
        orgColor = image[sr][sc]

        if orgColor == color:
            return image
        
        image[sr][sc] = color
        
        delta = [(0,1), (1,0), (0,-1), (-1,0)]

        while queue:
            curri, currj = queue.popleft()
            

            for dx, dy in delta:
                newi = curri + dx 
                newj = currj + dy
                if 0 <= newi < len(image) and 0 <= newj < len(image[0]) and image[newi][newj] == orgColor:
                    queue.append((newi, newj))
                    image[newi][newj] = color


        return image



        
# @lc code=end

