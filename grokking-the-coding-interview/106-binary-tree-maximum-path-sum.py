# Definition of a binary tree node
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
import sys
from ds_v1.BinaryTree.BinaryTree import TreeNode


def max_path_helper(root, max_path):
    if root == None:
        return 0
    
    left = max_path_helper(root.left, max_path)
    right = max_path_helper(root.right, max_path)
    
    max_path[0] = max(max_path[0], root.data + left + right)
    
    return max(left, right) + root.data

def max_path_sum(root):
    
    # Replace this placeholder return statement with your code
    max_path = [-sys.maxsize]
    
    max_path_helper(root, max_path)
    return max_path[0]
    
    
    
    
    