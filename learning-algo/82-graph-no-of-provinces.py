from networkx.utils import UnionFind

def find_no_provinces(grid):
    uf = UnionFind()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                # Check the four neighbors (up, down, left, and right) of the current cell
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + dx, j + dy
                    # If the neighbor is within the grid and contains a 1, union the current cell and the neighbor
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[i]) and grid[ni][nj] == 1:
                        uf.union((i, j), (ni, nj))

    provinces = set()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                # Add the set representative of each city to the provinces set
                provinces.add(uf[(i, j)])

    # The number of provinces is the number of unique set representatives
    return len(provinces)

grid = [[0,0,0], [1,0,1], [0,0,0]]
print(find_no_provinces(grid))  # Output: 2