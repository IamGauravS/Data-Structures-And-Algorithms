from ds_v1.BinaryTree.BinaryTree import TreeNode

# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

def flatten_tree(root):

    # Replace this placeholder return statement with your code
    if root is None:
        return 
    
    ##The function works by first flattening the left subtree, then moving it to the right, and finally attaching the flattened right subtree at the end. If you flatten the right subtree before the left, the right subtree would get detached when you move the left subtree to the right, and you would lose the reference to it.
    flatten_tree(root.left)  
    flatten_tree(root.right)
    
    right_subtree = root.right
    
    root.right = root.left
    root.left = None 
    
    current = root 
    while current.right:
        current = current.right 
        
    current.right = right_subtree
    
    return root 
