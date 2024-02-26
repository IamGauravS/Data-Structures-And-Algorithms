## initially everyone is parent of itself
## if we attach two with same rank then only we increase rank
class disjointset:
    def __init__(self, size):
        self.parent = [-1 for i in range(size)]
        self.rank = [0 for i in range(size)]
    def find(self, x):
        if self.parent[x] == -1:
            return x 
        self.parent[x] = self.find(self.parent[x]) ## implements path compression
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y
                self.rank[root_x] +=1 

    def is_same_set(self, x, y):
        return self.find(x) == self.find(y)
    

ds = disjointset(10)

ds.union(0, 1)
ds.union(2, 3)
ds.union(4, 5)
ds.union(6, 7)
ds.union(1, 3)
ds.union(5, 7)

print(ds.is_same_set(0, 2))  # False
print(ds.is_same_set(1, 6)) 
    