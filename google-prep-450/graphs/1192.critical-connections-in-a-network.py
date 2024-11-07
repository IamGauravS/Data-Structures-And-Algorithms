#
# @lc app=leetcode id=1192 lang=python3
#
# [1192] Critical Connections in a Network
#

# @lc code=start
class Solution:
    def dfs(self, node, parent, visited, tinsertion, tlow, bridges, adjList):
        visited[node] = True
        tinsertion[node] = tlow[node] = self.time
        self.time += 1

        # Traverse each neighbor of the current node
        for neighbor in adjList[node]:
            if neighbor == parent:
                continue
            if not visited[neighbor]:
                # Recur for unvisited neighbor
                self.dfs(neighbor, node, visited, tinsertion, tlow, bridges, adjList)
                
                # Update the lowest time reachable for `node`
                tlow[node] = min(tlow[node], tlow[neighbor])

                # Check if the edge is a bridge
                if tlow[neighbor] > tinsertion[node]:
                    bridges.append([node, neighbor])
            else:
                # Update the lowest time if back edge found
                tlow[node] = min(tlow[node], tinsertion[neighbor])

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # Initialize graph and helper data structures
        self.time = 0
        adjList = defaultdict(list)
        for src, dest in connections:
            adjList[src].append(dest)
            adjList[dest].append(src)

        visited = [False] * n
        tinsertion = [-1] * n
        tlow = [-1] * n
        bridges = []

        # Start DFS from the first node
        self.dfs(0, -1, visited, tinsertion, tlow, bridges, adjList)

        return bridges

# @lc code=end

