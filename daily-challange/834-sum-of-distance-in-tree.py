from collections import defaultdict

class Solution:
    def findMinDistance(self, src, target, parent):
        if self.dp[src][target] != float('inf'):
            self.dp[target][src] = self.dp[src][target]
            return self.dp[src][target]
        
        if self.dp[target][src] != float('inf'):
            self.dp[src][target] = self.dp[target][src]
            return self.dp[src][target]
        
        if src == target:
            self.dp[src][target] = 0
            return 0
        
        minDistance = float('inf')

        for child in self.adjList[src]:
            if child != parent:
                minDistance = min(minDistance, self.findMinDistance(child, target, src))

        self.dp[src][target] = 1 + minDistance 

        return self.dp[src][target]

        


        

    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:

        self.dp = [[float('inf') for i in range(n)] for j in range(n)]

        self.adjList = defaultdict(list)

        for node1, node2 in edges:
            self.adjList[node1].append(node2)
            self.adjList[node2].append(node1)

        for i in range(n):
            self.dp[i][i] = 0

        for src in range(n):
            for target in range(n):
                if self.dp[src][target] == float('inf'):
                    self.findMinDistance(src, target, -1)


        distances = []
        for i in range(n):
            distances.append(sum(self.dp[i]))

        return distances
