## terminal node outdegree of the node is zero  ## all paths should end up at a terminal node

## here we are checking for each node and only including those nodes for which any path do not lead to a cycle
import queue
def detect_terminal_node(graph):
    safe_nodes = []
    for node in graph.keys():
        visited = [False for i in range(len(graph))]
        q = queue.Queue()
        q.put(node)
        flag = True
        while not q.empty():
            curr_node = q.get()
            if visited[curr_node] == True:
                flag = False
                break
            else:
                visited[curr_node] = True 
                for child in graph[curr_node]:
                    if visited[child] == True:
                        flag =  False
                        break
                    else:
                        q.put(child)

        if flag:
            safe_nodes.append(node)

    return safe_nodes
