
## left should be less than node and right should be greater than node for all children

def binary_tree(root, value):
    if root == None:
        return False 
    
    if root.data == value:
        return True 
    
    elif root.data > value:
        return binary_tree(root.left, value)
    
    else:
        return binary_tree(root.right, value )