# Definition of a binary tree node
#
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

from ds_v1.BinaryTree.BinaryTree import TreeNode

def serialize_helper(root, output):
    if root == None:
        output.append(None)
        return 
    
    output.append(root.data)
    serialize_helper(root.left, output)
    serialize_helper(root.right, output)
    
    return 

def serialize(root):

    # Replace this placeholder return statement with your code
    output = []
    if root is None:
        return [None]
    serialize_helper(root, output)
    return output

def deserialize(stream):
    
   # Replace this placeholder return statement with your code
    if stream[0] is None:
        stream.pop(0)
        return None 
    
    root = TreeNode(stream[0])
    stream.pop(0)
    root.left = deserialize(stream)
    root.right = deserialize(stream)
    return root 