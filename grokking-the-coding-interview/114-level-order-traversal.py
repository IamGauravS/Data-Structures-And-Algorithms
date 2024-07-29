# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

import queue
from ds_v1.BinaryTree.BinaryTree import TreeNode

def level_order_traversal(root):

    # Replace this placeholder return statement with your code
    curr_queue = queue.Queue()
    next_queue = queue.Queue()
    
    curr_queue.put(root)
    
    output = ""
    if root ==None:
        return "None"
    while not curr_queue.empty():
        elem = curr_queue.get()
        if len(output) > 0 and output[-2] != ':':
            output= output + ', ' + str(elem.data)
        elif len(output) > 0 and output[-2] == ':':
            output= output  + str(elem.data)
        else:
            output = output + str(elem.data)
        
        
        if elem.left:
            next_queue.put(elem.left)
        if elem.right:
            next_queue.put(elem.right)
            
        if curr_queue.empty():
            output = output + ' : '
            curr_queue, next_queue = next_queue, curr_queue 
            
    return output[:-3]