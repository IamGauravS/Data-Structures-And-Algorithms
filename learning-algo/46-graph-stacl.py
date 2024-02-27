## graph = {1:[2,3,4], 2:[4,5] ....}

def dfs(graph, starting_node):
    stack  = []
    stack.append(starting_node)

    visited = [False] * len(max(graph.keys()) + 1)
    while len(stack) !=0:
        curr = stack.pop()
        print(curr)
        visited[curr] = True 
        for children in graph[curr]:
            if visited[children] == False:
                stack.append(children)


    return 
