
import queue

def right_side_view(root):
    
    if root is None:
        return []
    q = queue.Queue()
    q.put(root)
    output = []
    
    while not q.empty():
        q_size = q.qsize()
        temp = []
        for _ in range(q_size):
            curr = q.get()
            temp.append(curr.data)
            
            if curr.left:
                q.put(curr.left)
                
            if curr.right:
                q.put(curr.right)
                
        output.append(temp)
        
        
        
    final_output = [o[-1] for o in output]
    return final_output
        
    
                