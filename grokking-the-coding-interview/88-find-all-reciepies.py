from collections import deque

def find_recipes(recipes, ingredients, supplies):
    
    # Replace this placeholder return statement with your code
    graph = {}
    for i, ing in enumerate(ingredients):
        for j in ing:
            if j not in graph:
                graph[j] = []
            graph[j].append(recipes[i])
        
        
    indegre = {}
    for i , rec in enumerate(recipes):
        indegre[rec] = len(ingredients[i])
        
    q  = deque()
    
    for supp in supplies:
        q.append(supp)
        
    topo = []
    while q:
        curr = q.popleft()
        if curr in indegre and indegre[curr] ==0:
            topo.append(curr)
        if curr in graph:
            for child in graph[curr]:
                indegre[child] -=1
                if indegre[child] == 0:
                    q.append(child)
                    
    return topo
