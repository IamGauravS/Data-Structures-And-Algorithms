from EduBinaryTree import *
from EduTreeNode import *

import queue
def connect_all_siblings(root):

    # Replace this placeholder return statement with your code
    if root is None:
        return root 
    
    q = queue.Queue()
    prev = None 
    q.put(root)
    
    while q:
        curr = q.get()
        if prev != None:
            prev.next = curr 
            
        if curr.left:
            q.put(curr.left)
        if curr.right:
            q.put(curr.right)
            
        prev = curr 
        
    if prev is not None:
        prev.next = None 
    return root



