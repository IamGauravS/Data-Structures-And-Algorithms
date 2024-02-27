from Graph import Graph
# We only need Graph for this Question!


def num_edges(g):
    # For undirected graph, just sum up the size of
    # all the adjacency lists for each vertex
    sum = 0
    for i in range(g.vertices):
        temp = g.array[i].head_node
        while temp is not None:
            sum += 1
            temp = temp.next_element

    # Half the total sum as it is an undirected graph
    return sum//2