from ds_v1.BinaryTree.BinaryTree import TreeNode

# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None


def is_same(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.data != root2.data:
        return False 

    left_same = is_same(root1.left, root2.left)
    right_same = is_same(root1.right, root2.right)
    return left_same and right_same

def is_subtree(root, sub_root):
    
    # Replace this placeholder return statement with your code
    stack = []
    stack.append(root)
    while stack:
        curr = stack.pop()
        if is_same(curr, sub_root):
            return True 
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)

    return False 