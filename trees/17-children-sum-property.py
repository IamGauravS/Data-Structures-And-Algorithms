

## for any node the value must be equal to left + right and u can increment the node value to make it fulfil the property
## u can increase the value but not decrease

def children_sum_property(root):
    if root == None:
        return 
    
    child = 0 
    if root.left:
        child += root.left.data 
    if root.right:
        child += root.right.data 
        
    if child > root.data:
        root.data = child 
        
    else:
        if root.left:
            root.left.data = root.data 
        elif root.right:
            root.right.data = root.data 
            
    children_sum_property(root.left)
    children_sum_property(root.right)
    
    tot = 0
    if root.left:
        tot += root.left.data 
    if root.right:
        tot += root.right.data 
        
    if root.left or root.right:  ##check for leaf node
        root.data = tot 
        
        
    return root 
    
    
    
        