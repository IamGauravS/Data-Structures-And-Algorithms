class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        
    def add(self, key):
        if key not in self.parent:
            self.parent[key] = key 
            self.rank[key] = 0
            
    def union(self, key1, key2):
        parent1 = self.find(key1)
        parent2 = self.find(key2)
        
        if parent1 != parent2:
            if self.rank[parent1] > self.rank[parent2]:
                self.parent[parent2] = parent1
            else:
                self.parent[parent1] = parent2
                if self.rank[parent1] == self.rank[parent2]:
                    self.rank[parent2] += 1
                    
    def find(self, key):
        if self.parent[key] != key:
            self.parent[key] = self.find(self.parent[key])
        return self.parent[key]
        
        

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        djs = DisjointSet()
        
        for edge in edges:
            djs.add(edge[0])
            djs.add(edge[1])
            
            if djs.find(edge[0]) != djs.find(edge[1]):
                djs.union(edge[0], edge[1])
            else:
                output = edge 
                
                
        return output