# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

from ds_v1.BinaryTree.BinaryTree import TreeNode

def rob_helper(node, isparentrobed):
    if node == None:
        return 0

    if isparentrobed:
        return rob_helper(node.left, False) + rob_helper(node.right, False)
    else:
        rob = node.data + rob_helper(node.left, True) + rob_helper(node.right, True)
        not_rob = rob_helper(node.left, False) + rob_helper(node.right, False)
        return max(rob, not_rob)

def rob(root):
    return rob_helper(root, False)