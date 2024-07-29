def estimate_water_flow_helper(heights, i, j, output_grid, visited):
    if visited[i][j]:
        return output_grid[i][j]
    
    visited[i][j] = True
    delta = [(0,1), (1,0), (0,-1), (-1,0)]
    if i ==0 or j==0:
        output_grid[i][j][0] = 1 
    if i == len(heights) -1 or j == len(heights[0]) -1:
        output_grid[i][j][1] = 1
    for dx, dy in delta:
        neighbori = i+dx 
        neighborj = j+dy 
        
        if  0 <= neighbori < len(heights) and 0 <= neighborj < len(heights[0]) and heights[i][j] >= heights[neighbori][neighborj]:
            flow = estimate_water_flow_helper(heights, neighbori, neighborj, output_grid, visited)
            if flow[0] > output_grid[i][j][0]:
                output_grid[i][j][0] = flow[0]
            if flow[1] > output_grid[i][j][1]:
                output_grid[i][j][1] = flow[1] 
                
    return output_grid[i][j] 


def estimate_water_flow(heights):
    
    # Replace this placeholder return statement with your code
    
    
    length = len(heights)
    width = len(heights[0])
    
    output_grid = [[[-1,-1] for i in range(width)] for j in range(length)]
    visited = [[False for i in range(width)] for j in range(length)]
    
    for i in range(length):
        for j in range(width):
            if output_grid[i][j] == [-1,-1]:
                estimate_water_flow_helper(heights, i, j, output_grid, visited)
                
    no_of_heights_for_both_ocean = []
    for i in range(length):
        for j in range(width):
            if output_grid[i][j] == [1,1]:
                no_of_heights_for_both_ocean.append([i,j])
                
    return no_of_heights_for_both_ocean
    