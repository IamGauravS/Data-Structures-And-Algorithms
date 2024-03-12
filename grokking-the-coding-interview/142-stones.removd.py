def remove_stones(stones):

    offset = 100000
    stone = UnionFind()

    for x, y in stones:
        stone.union(x, (y + offset))  
    
    groups = set()
    for i in stone.parents:
        groups.add(stone.find(i))

    return len(stones) - len(groups)