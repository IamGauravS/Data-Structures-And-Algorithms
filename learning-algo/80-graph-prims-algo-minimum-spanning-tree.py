import heapq

def prims_algorithm(graph, no_of_vertices):
    visited = [False for i in range(no_of_vertices)]

    mst = []
    heap = []
    ## wt, node, parent
    heapq.heappush(heap, [0,0,-1])
    
    while heap:
        curr = heapq.heappop()
        if visited[curr[1]] == True:
            continue
        visited[curr[1]] = True
        if curr[1] != -1:
            mst.append([curr[2], curr[1]])
        for child in graph[curr[1]]:
            if visited[child[0]] == False:
                heapq.heappush(heap, [child[1], child[0], curr[1]])

    return mst
