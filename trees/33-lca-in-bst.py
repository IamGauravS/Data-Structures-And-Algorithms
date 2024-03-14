def find_lowest_common_ancestor(root, a, b):   ### normal tree 
    if root is None:
        return None

    if root.data == a or root.data == b:
        return root

    left = find_lowest_common_ancestor(root.left, a, b)
    right = find_lowest_common_ancestor(root.right, a, b)

    if left and right:
        return root  # If a and b are on both sides, then root is LCA
    else:
        return left if left else right  # Else return the non-null value
    
    
    
def find_lowest_common_ancestor_in_bst(root, a, b):
    if root is None:
        return None
    
    # If both a and b are greater than the root's value,
    # LCA lies in the right subtree
    if a > root.data and b > root.data:
        return find_lowest_common_ancestor_in_bst(root.right, a, b)
    
    # If both a and b are less than the root's value,
    # LCA lies in the left subtree
    elif a < root.data and b < root.data:
        return find_lowest_common_ancestor_in_bst(root.left, a, b)
    
    # If one is greater and one is smaller or equal, or they are equal,
    # the current node is the LCA
    else:
        return root