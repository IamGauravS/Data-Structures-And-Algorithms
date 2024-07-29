
from disjoint_set import DisjointSet
def kruskals_algorithm(edges):
    ds = DisjointSet()
    
    for edge in edges:
        src, dest, wt = edge 
        ds.add(src)
        ds.add(dest)
        
    edges = sorted(edges, key = lambda x : x[2])
    
    mst_edges = []
    
    for edge in edges:
        src, dest, wt = edge 
        if ds.find(src) != ds.find(dest):
            ds.union(src, dest)
            mst_edges.append(edge)
            
    return mst_edges