
import queue 
def print_nodes(root, target_node, target):
    
    parent_map = {}
    q = queue.Queue()
    q.put((root, None))
    
    while not q.empty():
        qsize = q.qsize()
        curr = q.get()
        node = curr[0]
        parent = curr[1]
        parent_map[node] = parent 
        if node.left:
            q.put((node.left, node))
            
        if node.right:
            q.put((node.right, node))
            
            
    visited = {}
    for key in parent_map.keys():
        visited[key] = False
        
    distance = 0
    q = queue.Queue()
    q.put((target_node, distance))
    visited[target_node] = True 
    output = []
    while q:
        curr = q.get()
        node= curr[0]
        dest = curr[1]
        if dest == target:
            output.append(node.data)
        if node.left:
            if visited[node.left] == False:
                q.put((node.left, dest+1))
                visited[node.left] = True
        if node.right:
            if visited[node.right] == False:
                q.put((node.right, dest+1))
                visited[node.right] = True
        if parent_map[node]:
            if visited[parent_map[node]] == False:
                q.put((parent_map[node], dest+1))
                visited[parent_map[node]] = True 
                
    return output
        
        
    
        
    