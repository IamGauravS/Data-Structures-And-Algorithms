# Definition of a binary tree node
#
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

from ds_v1.BinaryTree.BinaryTree import TreeNode

def build_tree(p_order, i_order):

    # Replace this placeholder return statement with your code
    if not p_order:
        return None 
    
    root_value = p_order[0]
    root = TreeNode(root_value)
    
    i_order_index = i_order.index(root_value)
    
    root.left = build_tree(p_order[1:i_order_index+1], i_order[:i_order_index])
    root.right = build_tree(p_order[i_order_index+1:], i_order[i_order_index+1: ])
    
    return root