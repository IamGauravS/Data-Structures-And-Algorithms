## here each edge has a weight
## we are assuming 0 to always be source node
## it will be a list of pair {node: [{target_node1, weight1}, {target_node2, weight2} ..], node2 : []}
## step1 : do  a toposort on the graph
## step2:  create a distance array with source distance zero
## step3: take the nodes out of stack 1 by 1 and relax the edges
## step4: figure out adj node and update the distance


import sys 

def do_toposort(graph, topo, visited, node):
    visited[node] = True 
    for child in graph[node]:
        if visited[child[0]] == False:
            do_toposort(graph, topo, visited, child[0])
    
    topo.append(node)

#This code first performs a topological sort on the graph, then initializes a distance dictionary with a maximum value for all nodes except the source. It then iterates over the nodes in the topological order, and for each node, it relaxes all the edges from that node to its children. The distance to a child is updated if a shorter path to it is found. The function finally returns the shortest distances from the source to all other nodes.
def find_distance_from_source(graph, source):
    topo = []
    visited = {}
    for node in graph.keys():
        visited[node] = False 

    for node in graph.keys():
        if visited[node] == False:
            do_toposort(graph, topo, visited, node)

    distance = {}
    for node in graph:
        distance[node] = sys.maxsize
    
    distance[source] = 0

    while topo:
        curr = topo.pop()

        for child in graph[curr]:
            ch = child[0]
            wt = child[1]

            if distance[curr] + wt < distance[ch]:
                distance[ch] = distance[curr] + wt

    return distance 
