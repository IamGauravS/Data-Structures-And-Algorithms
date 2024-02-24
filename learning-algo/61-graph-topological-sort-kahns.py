import queue

def topological_sort(graph):
    # Initialize the in-degree list with zeros
    indegree = [0 for i in range(len(graph))]

    # Calculate the in-degree for each node
    for node in graph:
        for child in graph[node]:
            indegree[child] +=1

    # Initialize the queue
    q = queue.Queue()

    # Add nodes with zero in-degree to the queue
    for node in graph:
        if indegree[node] == 0:
            q.put(node)
    
    # Initialize the list to store the topological order
    topo = []

    # Process nodes until the queue is empty
    while not q.empty():
        # Get a node from the queue
        node = q.get()

        # Add the node to the topological order
        topo.append(node)

        # Node is in topo so remove from indegree
        for child in graph[node]:
            # Decrease the in-degree of the child node
            indegree[child] -= 1

            # If the in-degree of the child node is zero, add it to the queue
            if indegree[child] == 0:
                q.put(child)

    # Check if the topological sort includes all nodes
    if len(topo) == len(graph):
        # If it does, return the topological order
        return topo
    else:
        # If it doesn't, return an empty list (the graph has a cycle)
        return []