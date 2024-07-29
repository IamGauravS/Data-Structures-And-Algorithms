from disjoint_set import DisjointSet

def maximum_stones_removed(stones):
    max_row = max(stone[0] for stone in stones)
    max_col = max(stone[1] for stone in stones)
    
    ds = DisjointSet(max_row + max_col + 2)
    stone_nodes = {}
    
    for stone in stones:
        node_row = stone[0]
        node_col = stone[1] + max_row + 1
        ds.union(node_row, node_col)
        stone_nodes[node_row] = 1
        stone_nodes[node_col] = 1

    cnt = sum(1 for node in stone_nodes if ds.find(node) == node)
    
    return len(stones) - cnt