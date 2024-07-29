import queue
def serialize_tree(root):
    seriealized = []
    q = queue.Queue()
    q.put(root)
    
    while not q.empty():
        curr = q.get()
        if curr:
            seriealized.append(str(curr.data))
        
            q.put(curr.left)
            q.put(curr.right)
        else:
            seriealized.append('#')
            
    return ','.join(seriealized)


def deserialize_tree(data):
    if len(data) == 0 or data == '#':
        return None 
    
    elements = data.split(',')
    root = TreeNode(int(elements[0]))
    q = queue.Queue()
    q.put(root)
    
    i = 1
    
    while not q.empty() and i < len(elements):
        curr = q.get()
        if elements[i] != '#':
            curr.left = TreeNode(int(elements[i]))
            q.put(curr.left)
            
        i+=1 
        if i <len(elements) and elements[i] != '#':
            curr.right = TreeNode(int(elements[i]))
            q.put(curr.right)
            
        i +=1
    return root 
    
    
    