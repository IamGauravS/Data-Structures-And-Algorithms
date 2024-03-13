def boundry_traversal(root):
    ## anticlock wise boundry traversal
    
    ## 1. left boundry excluding leaves
    ## 2. get leaves
    ## 3. right boundry in reverse excluding leaves
    
    def get_left(root, left_output):
        if root is None:
            return 
        if not root.left and not root.right:  ## excluding leaf nodes
            return 
        left_output.append(root.data)
        if root.left:
            get_left(root.left, left_output)
        else:
            get_left(root.right, left_output)
            
    def get_right(root, right_output):
        if root is None:
            return 
        if not root.left and not root.right:  ## excluding leaf nodes
            return 
        if root.right:
            get_right(root.right, right_output)
        else:
            get_right(root.left, right_output)
            
        right_output.append(root.data)
    
    def get_leaves(root, leaves):
        if root is None:
            return 
        if not root.left and not root.right:
            leaves.append(root.data)
            return 
        if root.left:
            get_leaves(root.left, leaves)
        if root.right:
            get_leaves(root.right, leaves)
            
    if root == None:
        return []
    
    left_output = []
    get_left(root.left, left_output)
    leaves = []
    get_leaves(root, leaves)
    right_output = []
    get_right(root.right, right_output)
    
    return [root.data] + left_output + leaves + right_output
    
    
    
    