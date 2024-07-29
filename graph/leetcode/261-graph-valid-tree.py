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
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ds = DisjointSet()
        for i in range(n):
            ds.add(i)
            
        for edge in edges:
            ai, bi = edge 
            if ds.find(ai) != ds.find(bi):
                ds.union(ai, bi)
                
            else:
                return False 
            
        root = ds.find(0)
        for i in range(1, n):
            if ds.find(i) != root:
                return False 
            
        return True