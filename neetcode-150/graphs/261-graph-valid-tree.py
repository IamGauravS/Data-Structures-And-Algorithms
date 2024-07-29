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
    
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        disjointset = DisjointSet()
        
        
        for i in range(n):
            disjointset.add(i)
            
        for edge in edges:
            if disjointset.find(edge[0]) != disjointset.find(edge[1]):
                disjointset.union(edge[0], edge[1])
            else:
                return False ## there is a cycle
            
        root = disjointset.find(0) ## check if all nodes are connected
        ## if they are connected they will have same parent
        for i in range(1, n):
            if disjointset.find(i) != root:
                return False 
            
        return True
                
        
        