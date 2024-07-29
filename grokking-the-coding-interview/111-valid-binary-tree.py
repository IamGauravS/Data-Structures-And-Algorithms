# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

from ds_v1.BinaryTree.BinaryTree import TreeNode
import math

def validate_bst_helper(node, lower=float('-inf'), upper=float('inf')):
    if not node:
        return True

    if not lower < node.data < upper:
        return False

    if not validate_bst_helper(node.left, lower, node.data):
        return False
    if not validate_bst_helper(node.right, node.data, upper):
        return False
    return True

def validate_bst(root):
    return validate_bst_helper(root)





## d0 an inorder traversal all numbers must be sorted
def validate_bst_helper(root, prev):
    if not root:
         return True

    if not validate_bst_helper(root.left, prev):
        return False

    if root.data <= prev[0]:
        return False
    prev[0] = root.data

    return validate_bst_helper(root.right, prev)



def validate_bst(root):
    prev = [-math.inf]
    return validate_bst_helper(root, prev)