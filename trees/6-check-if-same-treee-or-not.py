def if_tree_same(root1, root2):
    
    if root1 == None and root2 == None:
        return True 
    
    if root1 == None:
        return False 
    if root2 == None:
        return False 
    
    if root1.data == root2.data:
        left = if_tree_same(root1.left, root2.left)
        right =if_tree_same(root1.right, root2.right)
        
        if left == True and right == True:
            return True 
        
    return False