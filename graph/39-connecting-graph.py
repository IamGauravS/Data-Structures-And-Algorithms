
from disjoint_set import DisjointSet
def connecting_graph(edges):
    ds = DisjointSet()
    
    for edge in edges:
        src, dest, wt = edge 
        
        ds.add(src)
        ds.add(dest)
        
        if ds.find(src) != ds.find(dest):
            ds.union(src, dest)
            
    total_no_of_connected_components = ds.get_num_sets()
    
    return total_no_of_connected_components -1