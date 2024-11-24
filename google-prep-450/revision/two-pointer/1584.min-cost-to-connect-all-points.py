#
# @lc app=leetcode id=1584 lang=python3
#
# [1584] Min Cost to Connect All Points
#

# @lc code=start
from collections import defaultdict

class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False

        # Union by rank
        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1

        return True

class Solution:
    def getManHattenDistance(self, point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        edges = []
        BASE = 10**7
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                edges.append([ self.getManHattenDistance(points[i], points[j]) ,i, j])

        
        edges.sort()
        minCost = 0
        uf = UnionFind(len(points))
        edgesUsed = 0
        
        for cost, i, j in edges:
            if uf.union(i, j):
                minCost += cost 
                edgesUsed += 1
                if edgesUsed == len(points) - 1:
                    break 


        return minCost

        
# @lc code=end

