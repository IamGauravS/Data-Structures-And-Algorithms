# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
from ds_v1.BinaryTree.BinaryTree import TreeNode

def kth_smallest_element(root, k):
    def inorder(r):
        return inorder(r.left) + [r.data] + inorder(r.right) if r else []

    return inorder(root)[k - 1]
