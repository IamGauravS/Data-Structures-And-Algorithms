from disjoint_set import DisjointSet


def find_number_of_provinces(edges):
    ds = DisjointSet()
    
    for edge in edges:
        src, dest, wt = edge 
        ds.add(src)
        ds.add(dest)
        
        if ds.find(src) != ds.find(dest):
            ds.union(src, dest) 
            
            
    return ds.get_num_sets()  
    
        
        
        