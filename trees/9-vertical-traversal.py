import queue 

def vertical_traversal(root):
    if root is None:
        return 
    output = []
    
    q = queue.Queue()
    q.put([root,0])
    
    while not q.empty():
        curr =q.get()
        node = curr[0]
        level = curr[1]
        output.append([level, node.data])
        
        if node.left:
            q.put([level-1, node.left])
        if node.right:
            q.put([level+1, node.right])
            
        
    output = sorted(output, key = lambda x: x[0])
    
    output = [x[1] for x in output]
    return output
    
    
    
    