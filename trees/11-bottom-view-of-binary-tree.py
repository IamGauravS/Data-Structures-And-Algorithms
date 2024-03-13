import queue

def bottom_binary_tree(root):
    if root is None:
        return 
    
    q = queue.Queue()
    
    map_dict= {}
    
    q.put((0, root))
    
    while not q.empty():
        qsize = q.qsize()
        for _ in range(qsize):
            curr = q.get()
            level = curr[0]
            node = curr[1]
            if level not in map_dict:
                map_dict[level] = []
                
            map_dict[level].append(node.data)
            if node.left:
                q.put((level-1, node.left))
            if node.right:
                q.put((level+1, node.right))
                
    
    output = []
    sorted_keys = sorted(map_dict.keys())
    for keys in sorted_keys:
        output.append(map_dict[keys][-1])
        
    return output
        
    
    