# Definition of a binary tree node
#
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

from ds_v1.BinaryTree.BinaryTree import TreeNode

def mirror_binary_tree(root):
  
  # Replace this placeholder return statement with your code
  if root == None:
      return root 
  temp = root.left 
  root.left = root.right 
  root.right = temp 
  
  root.left = mirror_binary_tree(root.left)
  root.right = mirror_binary_tree(root.right)
  
  return root