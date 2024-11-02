#
# @lc app=leetcode id=323 lang=python3
#
# [323] Number of Connected Components in an Undirected Graph
#

# @lc code=start
from collections import defaultdict
class Solution:
    

    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adjList = defaultdict(list)

        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        visited = set()
        noOfComponents = 0

        def dfs(i):
            stack = []
            stack.append(i)
            visited.add(i)

            while stack:
                curr = stack.pop()
                for ch in adjList[curr]:
                    if ch not in visited:
                        visited.add(ch)
                        stack.append(ch)

            return 

        for i in range(n):
            if i not in visited:
                noOfComponents += 1
                dfs(i)


        

        return noOfComponents

        


        
# @lc code=end

