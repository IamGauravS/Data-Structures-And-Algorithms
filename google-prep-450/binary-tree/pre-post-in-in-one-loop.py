def traverse_all(root):
    if not root:
        return [], [], []  # Preorder, Inorder, Postorder

    preorder, inorder, postorder = [], [], []
    stack = [(root, 0)]  # Stack holds tuples of (node, state)

    while stack:
        node, state = stack.pop()

        if state == 0:  # Preorder: Visit Node
            preorder.append(node.val)
            stack.append((node, 1))  # Move to Inorder state
            if node.left:  # Push left child to stack
                stack.append((node.left, 0))  # State is 0 for left

        elif state == 1:  # Inorder: Visit Left Child
            inorder.append(node.val)
            stack.append((node, 2))  # Move to Postorder state
            if node.right:  # Push right child to stack
                stack.append((node.right, 0))  # State is 0 for right

        elif state == 2:  # Postorder: Visit Node
            postorder.append(node.val)

    return preorder, inorder, postorder
