from union_find import UnionFind


def redundant_connection(edges):
    
    # Replace this placeholder return statement with your code
    max_ele = -1
    for edge in edges:
        max_ele = max(max_ele, edge[0], edge[1])
        
    uf = UnionFind(max_ele+1)
    
    
    not_needed_edges = []
    for edge in edges:
        parent_s = uf.find_parent(edge[0])
        parent_d = uf.find_parent(edge[1])
        if parent_s != parent_d:
            uf.union(edge[0], edge[1])
        else:
            not_needed_edges.append(edge)
            
    return not_needed_edges[-1]
        
        
