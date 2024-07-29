class DisjointSet:
    def __init__(self, n):
        
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
        self.num_sets = n 
        
        
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
            
        return self.parent[i] 
    
    
    def union_by_rank(self, p, q):
        parent_p = self.find(p)
        parent_q = self.find(q)
        
        if parent_p != parent_q:
            if self.rank[parent_p] == self.rank[parent_q]:
                self.parent[parent_p]=  self.parent[parent_q] 
                self.rank[parent_p] += 1
                
            elif self.rank[parent_p] < self.rank[parent_q]:
                self.parent[parent_p] = parent_q
            else:
                self.parent[parent_q] = parent_p
                
        self.num_sets -= 1 
        
        
    def get_num_set(self):
        return self.num_sets
    
    
    
class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]  # Initialize size of each set to 1
        self.num_sets = n
        
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union_by_size(self, p, q):
        parent_p = self.find(p)
        parent_q = self.find(q)
        
        if parent_p != parent_q:
            if self.size[parent_p] < self.size[parent_q]:
                self.parent[parent_p] = parent_q
                self.size[parent_q] += self.size[parent_p]
            else:
                self.parent[parent_q] = parent_p
                self.size[parent_p] += self.size[parent_q]
            self.num_sets -= 1

    def get_num_sets(self):
        return self.num_sets
    
    
    
    
class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.num_sets = 0

    def add(self, element):
        if element not in self.parent:
            self.parent[element] = element
            self.rank[element] = 0
            self.num_sets += 1

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union_by_rank(self, p, q):
        if p not in self.parent or q not in self.parent:
            return
        parent_p = self.find(p)
        parent_q = self.find(q)

        if parent_p != parent_q:
            if self.rank[parent_p] == self.rank[parent_q]:
                self.parent[parent_p] = parent_q
                self.rank[parent_q] += 1
            elif self.rank[parent_p] < self.rank[parent_q]:
                self.parent[parent_p] = parent_q
            else:
                self.parent[parent_q] = parent_p
            self.num_sets -= 1

    def get_num_sets(self):
        return self.num_sets