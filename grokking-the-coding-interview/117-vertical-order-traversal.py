# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

from ds_v1.BinaryTree.BinaryTree import TreeNode
from collections import deque

def vertical_order(root):

    # Replace this placeholder return statament with your code
    if root is None:
        return []
    
    q = deque()
    q.append([root,0])
    output_dict = {}
    
    while q:
        curr_elem = q.popleft()
        node = curr_elem[0]
        column_index = curr_elem[1]
        
        if column_index not in output_dict:
            output_dict[column_index] = []
        output_dict[column_index].append(node.data)
        
        if node.left:
            q.append([node.left, column_index-1])
        if node.right:
            q.append([node.right, column_index+1])
            
    sorted_keys = sorted(output_dict.keys())
    output_list = []
    for key in sorted_keys:
        output_list.append(output_dict[key])
        
    return output_list