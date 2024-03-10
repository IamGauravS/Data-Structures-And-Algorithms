from EduBinaryTree import *
from EduTreeNode import *

from collections import deque
def populate_next_pointers(root):

    # Replace this placeholder return statement with your code
    
    if root is None:
        return root 
    
    q = deque([root])
    
    while q:
        
        prev = None 
        q_len = len(q)
        for _ in range(q_len):
            
            curr_elem = q.popleft()
            if prev != None:
                prev.next = curr_elem
                
            
            if curr_elem.left:
                q.append(curr_elem.left)
            if curr_elem.right:
                q.append(curr_elem.right)
                
            prev = curr_elem 
            
    return root
                
        
            
            