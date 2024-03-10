def if_tree_is_balanced(root):
    def check(root):
        if root == None:
            return 0 
        
        lh = check(root.left)
        rh = check(root.right)
        
        if lh == -1 or rh == -1 or abs(lh-rh) > 1:
            return -1 
        
        return 1 + max(lh, rh)
        
    return check(root) != -1