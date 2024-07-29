def count_complete_tree_nodes(root):
    if root is None:
        return 0

    d = depth(root)

    # If the tree has 2^d - 1 nodes, then we return the number of nodes
    if root and depth(root.right) == d - 1:
        return (2 ** d) - 1
    # Otherwise, we calculate the number of nodes in the left and right subtrees and add 1 (for the root)
    else:
        return 1 + count_complete_tree_nodes(root.left) + count_complete_tree_nodes(root.right)

def depth(node):
    # Compute the depth (height) of a tree
    d = 0
    while node:
        node = node.left
        d += 1
    return d