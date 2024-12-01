#
# @lc app=leetcode id=802 lang=python3
#
# [802] Find Eventual Safe States
#

# @lc code=start
from collections import defaultdict, deque
from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # Reverse graph and indegree tracking
        reverseGraph = defaultdict(list)
        outdegree = [0] * len(graph)

        # Build reverse graph and outdegree count
        for i, neighbors in enumerate(graph):
            outdegree[i] = len(neighbors)
            for neighbor in neighbors:
                reverseGraph[neighbor].append(i)

        # Queue for nodes with zero outdegree
        queue = deque([i for i in range(len(graph)) if outdegree[i] == 0])
        safeNodes = []

        # Process nodes with zero outdegree
        while queue:
            currNode = queue.popleft()
            safeNodes.append(currNode)

            for neighbor in reverseGraph[currNode]:
                outdegree[neighbor] -= 1
                if outdegree[neighbor] == 0:
                    queue.append(neighbor)

        # Return sorted list of safe nodes
        return sorted(safeNodes)

        
# @lc code=end

