
def construct_bst_helper(preorder, inorder):
    if len(preorder) == 0 or len(inorder) == 0:
        return None 
    
    root = TreeNode(preorder[0])
    index_i = inorder.index(preorder[0])
    
    inorder_left = inorder[:index_i]
    inorder_right = inorder[index_i+1:]
    
    preorder_left = preorder[1:len(inorder_left)+1]
    preorder_right = preorder[len(inorder_left)+1:]
    
    root.left = construct_bst_helper(preorder_left, inorder_left)
    root.right = construct_bst_helper(preorder_right, inorder_right)
    
    return root 


def construct_bst(preorder):
    inorder = sorted(preorder)
    
    root = construct_bst_helper(preorder, inorder)
    return root