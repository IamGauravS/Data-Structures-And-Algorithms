class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def add(self, value):
        if value in self.parent:
            return
        else:
            self.parent[value] = value
            self.rank[value] = 0

    def find(self, value):
        if self.parent[value] != value:
            self.parent[value] = self.find(self.parent[value])
        return self.parent[value]

    def union(self, value1, value2):
        root1 = self.find(value1)
        root2 = self.find(value2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] += 1

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ds = DisjointSet()
        removed_edge = None
        for edge in edges:
            ai, bi = edge 
            ds.add(ai)
            ds.add(bi)

            if ds.find(ai) != ds.find(bi):
                ds.union(ai, bi)
            else:
                removed_edge = [ai, bi]

        return removed_edge