# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

from ds_v1.BinaryTree.BinaryTree import TreeNode

def check_if_allindrom(l):
    start = 0
    end = len(l)-1
    while start < end:
        if l[start] != l[end]:
            return False 
        start +=1
        end -=1 
    return True

import queue
def is_symmetric(root):

  # Replace this placeholder return statement with your code
    if root == None:
        return True 
    
    q = queue.Queue()
    q.put(root)
    level = []
    while not q.empty():
        
        len_q = q.qsize()
        
        for _ in range(len_q):
            curr_elem = q.get()
            level.append(curr_elem.data if curr_elem else None)
            if curr_elem:
                q.put(curr_elem.left)
                q.put(curr_elem.right)
                
        if not check_if_allindrom(level):
            return False
        level = []
        
    return True