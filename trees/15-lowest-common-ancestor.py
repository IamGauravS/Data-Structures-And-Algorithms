def find_lowest_common_ancestor(root, a, b):
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