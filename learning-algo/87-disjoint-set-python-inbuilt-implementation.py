from disjoint_set import DisjointSet

ds = DisjointSet()

# Add some elements
ds.make_set(1)
ds.make_set(2)
ds.make_set(3)
ds.make_set(4)
ds.make_set(5)

# Union some sets
ds.union(1, 2)
ds.union(3, 4)

# Find the representative of a set
print(ds.find(1))  # Output: 1
print(ds.find(2))  # Output: 1

# Get the size of a set
print(ds.get_size(1))  # Output: 2

# Get all sets
print(ds.get_sets())  # Output: [[1, 2], [3, 4], [5]]