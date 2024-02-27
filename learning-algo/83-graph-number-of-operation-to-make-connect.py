## you can only use the edge already there and inorded to connect two vertices u need to take it out from there and use
## minimum edges that we need to remove so that all components are connected

from networkx.utils import UnionFind
def make_the_graph_connected(edges, no_of_vertices):
    ## we just need to figure out the number of connected components first
    ## we can only use those edges where even after taking it out the graph was still connected
    
    count_extra_edge = 0
    uf = UnionFind()

    for edge in edges:
        u = edge[0]
        v = edge[1]
        if uf[u] == uf[v]:
            count_extra_edge +=1 
        else:
            uf.union(u, v)

    components = set()
    for v in range(no_of_vertices):
        components.add(uf[v])

    no_of_edges_required = len(components) - 1
    if no_of_edges_required < count_extra_edge:
        return no_of_edges_required
    else:
        return -1
