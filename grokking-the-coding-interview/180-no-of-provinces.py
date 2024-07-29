from unionfind import UnionFind


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            else:
                self.parent[rootx] = rooty
                if self.rank[rootx] == self.rank[rooty]:
                    self.rank[rooty] += 1
    

def find_connected_cities(is_city_connected):
    n = len(is_city_connected)
    uf = UnionFind(n)
    
    for i in range(n):
        for j in range(n):
            if is_city_connected[i][j] == 1:
                uf.union(i, j)
                
    provinces = set()
    for i in range(n):
        provinces.add(uf.find(i))
        
    return len(provinces)
