

import queue
def find_maximum_width(root):
    if root == None:
        return 0 
    
    q = queue.Queue()
    q.put(root)
    levels = []
    max_width = 0
    while not q.empty():
        qsize = q.qsize()
        temp = []
        max_width = max(max_width, qsize)
        for _ in range(qsize):
            curr = q.get()
            temp.append(curr)
            if curr.left:
                q.put(curr.left)
            if curr.right:
                q.put(curr.right)
                
        levels.append(temp)
        
    return max_width
        
        
    
            