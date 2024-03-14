

def construct_tree(postorder, inorder):
    
    if len(postorder) == 0 or len(inorder) == 0:
        return None 
    
    len_postorder = len(postorder)
    node = TreeNode(postorder[len_postorder-1])
    
    idx = inorder.index(postorder[len_postorder-1])
    
    inorder_left = inorder[:idx]
    inorder_right = inorder[idx+1:]
    
    postorder_left = postorder[:len(inorder_left)]
    postorder_right = postorder[len(inorder_left):len(inorder_left)+len(inorder_right)]
    
    node.left = construct_tree(postorder_left, inorder_left)
    node.right = construct_tree(postorder_right, inorder_right)
    
    return node 