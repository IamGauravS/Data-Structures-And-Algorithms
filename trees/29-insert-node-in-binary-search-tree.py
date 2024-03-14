


def insert_node(root, key):
    if root is None:
        return TreeNode(key)
    curr = root 
    
    while curr:
        if curr.data > key:
            if curr.left:
                curr = curr.left
            else:
                curr.left = TreeNode(key) 
                break
        else:
            if curr.right:
                curr = curr.right
            else:
                curr.right = TreeNode(key)
                break 
                 
    return root
            
    