#
# @lc app=leetcode id=947 lang=python3
#
# [947] Most Stones Removed with Same Row or Column
#

# @lc code=start
from collections import defaultdict
class UnionFind:
    def __init__(self):
        self.parent = defaultdict(lambda: None)  # Corrected lambda syntax
        self.rank = defaultdict(int)

    def find(self, node):
        if self.parent[node] is None:
            self.parent[node] = node
        
        # Apply path compression
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        
        return self.parent[node]
    
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        # Only unite if they have different roots
        if root1 != root2:
            # Union by rank
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root2] > self.rank[root1]:
                self.parent[root1] = root2
            else:
                self.parent[root1] = root2
                self.rank[root2] += 1  
            

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        uf = UnionFind()
        for stone in stones:
            uf.union(stone[0], (10**5)+stone[1])

        uniqueParents = set()

        for stone in stones:
            uniqueParents.add(uf.find(stone[0]))
            uniqueParents.add(uf.find((10**5)+stone[1]))

        return len(stones) - len(uniqueParents)
            

        

        
# @lc code=end

