
import queue
def top_view_of_binary_tree(root):
    if root is None:
        return 
    q = queue.Queue()
    q.put((0, root))
    map_dict = {} ## line, node
    
    while not q.empty():
        
        qsize = q.qsize()
        for _ in range(qsize):
            curr = q.get()
            node = curr[1]
            level = curr[0]
            if level not in map_dict:
                map_dict[level] = []
                
            map_dict[level].append(node.data)
            if node.left:
                q.put((level-1, node.left))
            if node.right:
                q.put((level+1, node.right))
                
            
    sorted_keys = sorted(map_dict.keys())
    
    output = []
    for keys in sorted_keys:
        output.append(map_dict[keys][0])
        
    return output