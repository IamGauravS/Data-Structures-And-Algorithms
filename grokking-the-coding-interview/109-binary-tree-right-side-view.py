from ds_v1.BinaryTree.BinaryTree import TreeNode

# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

def right_side_view_helper(root, output_list, current_level):
    if root == None:
        return 
    
    if current_level == len(output_list):
        output_list.append(root.data)
        
    right_side_view_helper(root.right, output_list, current_level+1)
    right_side_view_helper(root.left, output_list, current_level+1)
    
    return 


def right_side_view(root):
  
  # Replace this placeholder return statement with your code
  if root == None:
      return 
  output_list = []
  current_level = 0
  right_side_view_helper(root, output_list, current_level)
  
  return output_list