#
# @lc app=leetcode id=2959 lang=python3
#
# [2959] Number of Possible Sets of Closing Branches
#

# @lc code=start
from typing import List, Tuple

class Solution:
    
    def dfs(self, node, path, dist, end, graph, all_paths):
        if node == end:
            all_paths.append((path[:], dist))
            return
        
        for neighbor, weight in graph[node]:
            if neighbor not in path:  # Avoid cycles
                path.append(neighbor)
                self.dfs(neighbor, path, dist + weight, end, graph, all_paths)
                path.pop()

    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        # Build the graph
        graph = {i: [] for i in range(n)}
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        all_paths = []
        start, end = 0, n - 1  # Assuming we want paths from node 0 to node n-1
        self.dfs(start, [start], 0, end, graph, all_paths)

        # Filter paths by maxDistance
        valid_paths = [path for path, dist in all_paths if dist <= maxDistance]

        # Count the number of valid sets of closing branches
        count = 0
        for path in valid_paths:
            count += 1 << (len(path) - 2)  # Each path can have multiple sets of closing branches

        return count

# @lc code=end

