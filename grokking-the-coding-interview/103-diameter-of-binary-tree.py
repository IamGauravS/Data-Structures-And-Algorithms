from ds_v1.BinaryTree.BinaryTree import TreeNode
# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

def calculate_height(root):
    if root == None:
        return 0
    return 1 + max(calculate_height(root.right), calculate_height(root.left))
    


def diameter_of_binaryTree(root):

  # Replace this placeholder return statement with your code
  
    if root is None:
        return 0 
    
    left_height = calculate_height(root.left)
    right_height = calculate_height(root.right)
    
    left_diameter = diameter_of_binaryTree(root.left)
    right_diameter = diameter_of_binaryTree(root.right)
    
    
     # Return the maximum of the following:
    # 1) Diameter of left subtree
    # 2) Diameter of right subtree
    # 3) Height of left subtree + height of right subtree
    
    return max(left_height+right_height, left_diameter, right_diameter)
