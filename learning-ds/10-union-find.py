class DisjointSet:
    def __init__(self, n):
        ## This list keeps track of the parent of each element. The index in the list represents an element, 
        #and the value at that index represents the parent of the element. If an element is the root of a tree 
        #(i.e., the representative of a set), it is its own parent. This is why the parent list is initialized 
        #with self.parent = [i for i in range(n)].
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            # Union by rank to optimize the tree height
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y
                self.rank[root_y] += 1
#When two trees are merged using the union operation, the tree with the smaller rank is attached to the root of the tree with the larger rank. This is done to ensure that the resulting tree is as balanced as possible, which helps optimize the performance of the find and union operations.

#If the two trees have the same rank, it means they have the same depth. When they are merged, the depth of the resulting tree will be greater by one. Therefore, we need to increment the rank of the new root.

#However, if the two trees have different ranks, the tree with the smaller rank is attached as a subtree of the tree with the larger rank. This does not increase the depth of the resulting tree, so the rank of the root does not need to be incremented.

#In other words, we only need to increment the rank when the ranks of the two roots are equal because that's the only case where the depth of the resulting tree increases.
# Example usage:
n = 5  # Number of elements
ds = DisjointSet(n)

ds.union(0, 1)
ds.union(1, 2)
ds.union(3, 4)

print("Are 0 and 2 in the same set?", ds.find(0) == ds.find(2))  # Output: True
print("Are 2 and 3 in the same set?", ds.find(2) == ds.find(3))  # Output: False
