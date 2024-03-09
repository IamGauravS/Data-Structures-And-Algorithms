# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

from ds_v1.BinaryTree.BinaryTree import TreeNode
from collections import deque

def find_max_depth(root):

    # Replace this placeholder return statement with your code
    if root == None:
        return 0 
    
    left_subtree_height = find_max_depth(root.left)
    right_subtree_height = find_max_depth(root.right)
    
    return 1+ max(left_subtree_height, right_subtree_height)
