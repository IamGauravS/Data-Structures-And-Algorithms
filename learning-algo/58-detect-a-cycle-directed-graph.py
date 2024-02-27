

def detect_cycle(graph):
    visited = [False for i in range(len(graph))]

    
    
    for node in graph.keys():
        stack = []
        if visited[node] == False:
            stack.append(node)

        
            while stack:
                curr = stack.pop()
                visited[curr] = True 

                for child in graph[curr]:
                    if visited[child] == True:
                        return True 
                    else:
                        stack.append(child)

    return False


graph = {
    0: [1, 3],
    1: [2],
    2: [4],
    3: [],
    4: []
}

print(detect_cycle(graph))  # Your function will incorrectly return True

