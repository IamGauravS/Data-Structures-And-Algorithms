
def unique_paths_helper(src, dp, visited, m,n):
    if src[0] == m-1 and src[1] == n-1:
        return 1
    
    if visited[src[0]][src[1]] == True:
        return dp[src[0]][src[1]]
    
    i = src[0]
    j = src[1]
    visited[i][j] = True 
    delta = [(0, 1), (1,0)]
    no_of_paths = 0
    for dx, dy in delta:
        if 0 <= i+dx < m and 0 <= j+dy <n:
            no_of_paths += unique_paths_helper((i+dx, j+dy), dp, visited, m, n)
            
    dp[i][j] = no_of_paths
    return no_of_paths

def unique_paths(m, n):

    # Replace this placeholder return statement with your code
    dp = [[-1 for i in range(n)] for j in range(m)]
    visited = [[False for i in range(n)] for j in range(m)]
    src = (0,0)
    
    no_of_unique_path = unique_paths_helper(src, dp, visited, m,n )
    
    return no_of_unique_path
    