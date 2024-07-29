from ds_v1.BinaryTree.BinaryTree import TreeNode

# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

def pre_ordre_traversal(root, output):
    if root is None:
        return 
    output.append(root.data)
    pre_ordre_traversal(root.left, output)
    pre_ordre_traversal(root.right, output)

def same_tree(p, q):

    # Replace this placeholder return statement with your code
    output1 = []
    pre_ordre_traversal(p, output1)
    output2 = []
    pre_ordre_traversal(q, output2)
    
    return output2 == output1
