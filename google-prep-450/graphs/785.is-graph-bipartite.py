#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start
from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colorDict = {}
        for i in range(len(graph)):
            colorDict[i] = -1 

        for i in range(len(graph)):
            if colorDict[i] == -1:
                queue = deque()
                queue.append(i)
                colorDict[i] = 0

                while queue:
                    curr = queue.popleft()
                    currColor = colorDict[curr]

                    for neighbor in graph[curr]:
                        if colorDict[neighbor] == -1:
                            if currColor:
                                colorDict[neighbor] = 0
                            else:
                                colorDict[neighbor] = 1
                            queue.append(neighbor)

                        else:
                            if colorDict[neighbor] == currColor:
                                return False
                    
        return True 

# @lc code=end

