import queue


### graph is a list of dictionary {1: [2,3,4], 2: [4,5,6]} ....
def bfs_traversal(graph, starting_node):
    q = queue.Queue()
    q.put(starting_node)
    visited = [-1]*len(graph)
    while not q.empty():
        curr_node = q.get()
        print(curr_node)
        visited[curr_node] = 1
        for children in graph[curr_node]:
            if visited[children] != 1:
                q.put(children)


    return 
                


