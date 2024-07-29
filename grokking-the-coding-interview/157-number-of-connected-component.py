from unionfind import UnionFind


def count_components(n, edges):

    # Replace this placeholder return statement with your code
    uf = UnionFind()
    for edge in edges:
        uf.add(edge[0])
        uf.add(edge[1])
        
    for edge in edges:
        src = edge[0]
        dest = edge[1]
        
        uf.union(src, dest)
            
            
    output_set = set()
    
    for edge in edges:
        output_set.add(uf.find(edge[0]))
        output_set.add(uf.find(edge[1]))
        
    return len(output_set)
        
    
