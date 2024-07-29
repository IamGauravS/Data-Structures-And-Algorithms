### only valid for directed graph
from collections import defaultdict
def find_strongly_connected_component(edges):
    
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        
    stack = []
    visited = set()
    
    ### first step is finding the finish distance last element in stack is the one with maximum finish time
    for node in graph:
        if node not in visited:
            dfs(graph, node, visited, stack)
            
            
    ## reverse the edges in graph
    transpose_graph = transpose(graph)
    
    
    ## find the order
    visited = set()
    output = []
    while stack:
        node = stack.pop()
        if node not in visited:
            scc = set()
            dfs(transpose_graph, node, visited, scc)
            output.append(scc)
    return output
            
            
            
def dfs(graph, node, visited, result):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, result)
    if isinstance(result, set):
        result.add(node)
    else:
        result.append(node)
        
        
def transpose(graph):
    transposed_graph = defaultdict(list)
    for node in graph:
        for neighbor in graph[node]:
            transposed_graph[neighbor].append(node)
            
    return transposed_graph



def find_unnecessary_edges(edges):
    # Existing code to find SCCs...
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    stack = []
    visited = set()

    for node in graph:
        if node not in visited:
            dfs(graph, node, visited, stack)

    transpose_graph = transpose(graph)

    visited = set()
    sccs = []
    while stack:
        node = stack.pop()
        if node not in visited:
            scc = set()
            dfs(transpose_graph, node, visited, scc)
            sccs.append(scc)

    # New code to find unnecessary edges...
    unnecessary_edges = []
    for u, v in edges:
        if not any(u in scc and v in scc for scc in sccs):
            unnecessary_edges.append((u, v))

    return unnecessary_edges