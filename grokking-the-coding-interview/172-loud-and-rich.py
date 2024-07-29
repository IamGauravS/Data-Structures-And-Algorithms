def dfs(i, res, visited, children, quiet):
    if visited[i] == True:
        return res[i]
    
    visited[i] = True
    
    for child in children[i]:
        v = dfs(child, res, visited, children, quiet)
        if quiet[v] < quiet[res[i]]:
            res[i] = v
        
    return res[i]

def loud_and_rich(richer, quiet):
  res = [i for i in range(len(quiet))]
  children = {i: [] for i in range(len(quiet))}
  
  for r, p in richer:
      children[p].append(r)
      
  visited = [False for _ in range(len(quiet))]
  
  for i in range(len(quiet)):
      if not visited[i]:
          dfs(i, res, visited, children, quiet)
      
  return res