
import queue

def zig_zag_traversal(root):
    
    q = queue.Queue()
    flag = 0 
    output = []
    
    q.put(root)
    
    while q:
        temp = []
        q_len = q.qsize()
        for _ in range(q_len):
            curr = q.get()
            temp.append(curr.data)
            if curr.left:
                q.put(curr.left)
            if curr.right:
                q.put(curr.right)
            
        if flag == 1:
            temp.reverse()
            flag = 0
        else:
            flag = 1 
            
        output.append(temp)
        