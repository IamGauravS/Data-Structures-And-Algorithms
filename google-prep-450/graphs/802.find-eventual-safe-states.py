#
# @lc app=leetcode id=802 lang=python3
#
# [802] Find Eventual Safe States
#

# @lc code=start
from collections import defaultdict, deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        reverseAdjList = defaultdict(list)
        indegree = {}

        for i in range(len(graph)):
            indegree[i] = 0

        for i in range(len(graph)):
            for nodes in graph[i]:
                reverseAdjList[nodes].append(i)
                indegree[i] += 1

        queue = deque()
        for i in range(len(graph)):
            if indegree[i] == 0:
                queue.append(i)

        safeNodes = []

        while queue:
            currNode = queue.popleft()
            safeNodes.append(currNode)

            for neighbor in reverseAdjList[currNode]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        safeNodes.sort()
        return safeNodes
                


        
# @lc code=end

