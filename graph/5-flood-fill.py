def flood_fill(matrix, src, newcolor):
    i, j = src
    oldcolor = matrix[i][j]

    if oldcolor == newcolor:
        return matrix

    def dfs(i, j):
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] != oldcolor:
            return

        matrix[i][j] = newcolor

        delta = [(0,1), (1,0), (0,-1), (-1,0)]
        for dx, dy in delta:
            dfs(i + dx, j + dy)

    dfs(i, j)
    return matrix