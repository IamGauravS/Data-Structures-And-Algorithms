
import queue
def minimum_time_taken_to_burn_tree_from_node(root, node):
    
    parent_map = {}
    q = queue.Queue()
    
    q.put((root, None))
    
    while not q.empty():
        curr = q.get()
        node = curr[0]
        parent = curr[1]
        parent_map[node] = parent 
        
        if node.left:
            q.put(node.left, node)
        if node.right:
            q.put(node.right, node)
            
    visited = {}
    for key in parent_map.keys():
        visited[key] = False
        
    max_distance = 0
    q = queue.Queue()
    q.put((node, 0))
    
    while not q.empty():
        curr = q.get()
        node = curr[0]
        dist = curr[1]
        max_distance = max(max_distance, dist)
        visited[node] = True 
        
        if node.left and visited[node.left] == False:
            visited[node.left] = True 
            q.put((node.left, dist+1))
            
        if node.right and visited[node.right] == False:
            visited[node.right] = True 
            q.put((node.right, dist+1))
            
        if parent_map[node] and visited[parent_map[node]] == False:
            visited[parent_map[node]] = True 
            q.put((parent_map[node], dist+1))
            
    return max_distance
            
    