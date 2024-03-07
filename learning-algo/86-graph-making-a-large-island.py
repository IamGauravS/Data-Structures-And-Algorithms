from disjoint_set import DisjointSet

def convert_ij_to_id(i, j, size):
    return i*size + j



def get_child(i,j, size, grid, type):
    delta = [(0,1), (1,0), (0,-1), (-1, 0)]
    children = []
    for dx, dy in delta:
        if 0 <= i+dx < size and 0 <= j+ dy < size:
            if grid[i+dx][j+dy] == type:
                children.append(convert_ij_to_id(i+dx, j+dy, size))
    return children
    

def make_large_island(grid):
    ds = DisjointSet()

    ## process the grid first
    size = len(grid)
    for i in range(size):
        for j in range(size):
            if grid[i][j] == 1:
                curr = convert_ij_to_id(i, j, size)
                ds.make_set(curr)
                children = get_child(i, j, size, grid, 1)
                for child in children:
                    if ds.find(curr) != ds.find(child):
                        ds.union(curr, child)

    maxsize = 1
    for i in range(size):
        for j in range(size):
            if grid[i][j] == 0:
                components = set()
                children = get_child(i, j, size, grid, 1)
                for child in children:
                    components.add(ds.find(child))

                compsize = 1  ## size should be included in new cell
                for comp in components:
                    compsize += ds.get_size(comp)

                if compsize > maxsize:
                    maxsize = compsize

    for i in range(size):
        for j in range(size):
            maxsize = max(maxsize, ds.get_size(convert_ij_to_id(i,j,size)))

    return maxsize

