from neighbors import neighbors
from backtracking import backtracking

# Tip: You may use some of the code templates provided
# in the support files
  
def word_search_helper(grid, word, i, x, y, visited):
    if i == len(word):
        return True 
    if x == len(grid) or y == len(grid[x]) or x<0 or y<0:
        return False
    
    
    if grid[x][y] != word[i] or (x,y) in visited:
        return False
    
    else:
        visited.add((x,y))
        p1 = word_search_helper(grid, word, i+1, x+1, y, visited)  ## check in same row
        p2 = word_search_helper(grid, word, i+1, x, y+1, visited)  ## check in same column
        p3 = word_search_helper(grid, word, i+1, x-1, y, visited)
        p4 = word_search_helper(grid, word, i+1, x, y-1, visited)
        visited.remove((x,y))
        return p1 or p2
    
def word_search(grid, word):
    
    # Replace this placeholder return statement with your code
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            flag = word_search_helper(grid, word, 0, i, j, set())
            if flag == True:
                return flag 
            
    return False
