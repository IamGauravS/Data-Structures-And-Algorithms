from collections import deque
from ds_v1.BinaryTree.BinaryTree import TreeNode

# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

import queue
def zigzag_level_order(root):

    # Replace this placeholder return statement with your code
    curr_queue = queue.Queue()
    next_queue = queue.Queue()
    output = []
    
    if root is None:
        return output 
    
    curr_queue.put(root)
    reverse_flag = False
    while not curr_queue.empty():
        temp = []
        while not curr_queue.empty():
            elem = curr_queue.get()
            temp.append(elem.data)
            if elem.left:
                next_queue.put(elem.left)
            if elem.right:
                next_queue.put(elem.right)
                
        if reverse_flag:
            temp.reverse()
            reverse_flag = False         
            output.append(temp)
        else:
            output.append(temp)
            reverse_flag = True
            
        curr_queue, next_queue = next_queue, curr_queue
        
    return output