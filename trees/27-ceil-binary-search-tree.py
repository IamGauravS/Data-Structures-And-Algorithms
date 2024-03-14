

## find smallest number greater than given value
def find_ceil(root, key):
    ceil = -1
    while (root):
        if root.data == key:
            ceil = root.data
            return ceil 
        
        if root.data < key:
            root =  root.right
            
        else:
            ceil = root.data
            root = root.left 
            
    return ceil