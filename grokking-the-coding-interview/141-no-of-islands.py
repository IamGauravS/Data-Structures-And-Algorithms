from union_find import UnionFind


def num_islands(grid):

    # Replace this placeholder return statement with your code
    uf = UnionFind(grid)
    
    hight = len(grid)
    width = len(grid[0])
    
    delta = [(0,1), (0,-1), (1, 0), (-1, 0)]
    
    for i in range(hight):
        for j in range(width):
            ij_inlist = i*width + j
            if grid[i][j] == '1':
                
                grid[i][j] = '0'
                
                for dx, dy in delta:
                    if 0 <= i+dx < hight and 0 <= j + dy < width and grid[i+dx][j+dy] == '1':
                        nin_list = (i+dx)*width + j+dy 
                        uf.union(ij_inlist, nin_list)
                    
                    
    return uf.get_count()
                    
            
            
