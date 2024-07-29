def construct_unique_trees(inorder, preorder):
    if not inorder or not preorder:
        return None

    node = TreeNode(preorder[0])
    idx = inorder.index(preorder[0])

    left = inorder[:idx]
    right = inorder[idx+1:]

    node.left = construct_unique_trees(left, preorder[1:len(left)+1])
    node.right = construct_unique_trees(right, preorder[len(left)+1:])

    return node





