def morris_traversal(root):
    current = root
    while current is not None:
        if current.left is None:
            print(current.data, end=" ")
            current = current.right
        else:
            # Find the inorder predecessor of current
            pre = current.left
            while pre.right is not None and pre.right != current:
                pre = pre.right

            # Make current as right child of its inorder predecessor
            if pre.right is None:
                pre.right = current
                current = current.left

            # Revert the changes made in the 'if' part to restore the original tree
            # i.e., fix the right child of predecessor
            else:
                pre.right = None
                print(current.data, end=" ")
                current = current.right