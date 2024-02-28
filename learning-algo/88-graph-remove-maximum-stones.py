from disjoint_set import DisjointSet 

def get_id(i,j,size):
    return i*size + j 

def remove_maximum_stones(grid):
    ds = DisjointSet()
    for i in range(len(grid)):
        ds.make_set(i)
    for j in range(len(grid[0])):
        ds.make_set(len(grid) + j)

    size = len(grid)

    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 1:
                id = get_id(i,j,size)
                ds.make_set(id)
                ds.union(i, id)
                ds.union(len(grid) + j, id)


    sets = ds.get_sets()
    no_of_stones = 0
    for s in sets:
        no_of_stones += len(s)
    
    no_of_stones = no_of_stones - 2*len(sets)
    return no_of_stones