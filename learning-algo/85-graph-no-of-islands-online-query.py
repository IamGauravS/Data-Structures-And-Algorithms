from networkx import UnionFind
5 = (1,0)
def get_id(i,j,size):
    return i*size + j

def get_child(i,j, size, grid):
    delta = [(0,1), (1,0), (0,-1), (-1, 0)]
    children = []
    for dx, dy in delta:
        if 0 <= i+dx < size and 0 <= j+ dy < size:
            if grid[i+dx][j+dy] == 1:
                children.append([i+dx, j+dy])
    return children

def number_of_island(queries, size):
    grid = [[0 for i in range(size)] for j in range(size)]
    uf = UnionFind()
    visited  = [[False for i in range(size)] for j in range(size)]

    no_of_island = 0
    for query in queries:
        i = query[0]
        j = query[1]
        if visited[i][j] == True:
            continue 
        visited[i][j] = True
        grid[i][j] = 1
        children = get_child(i, j, size, grid)
        if not children:
            print(no_of_island)
            continue
        for child in children:
            if uf[get_id(child[0], child[1])] != uf[get_id(i, j)]:
                uf.union(get_id(child[0], child[1]), get_id(i, j) )

        unique_island = set()
        for i in range(size):
            for j in range(size):
                id = get_id(i,j)
                unique_island.add(uf[id])
        print(no_of_island)
        print(len(unique_island))



