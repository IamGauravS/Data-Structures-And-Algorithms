
def print_root_to_node_helper(node, value, path):
    if node == None:
        return False 
    
    
    if value == node.data:
        path.append(node.data)
        return True 
    
    path.append(node.data)
    p1 = False 
    p2 = False
    if node.left:
        p1 = print_root_to_node_helper(node.left, value, path)
    if node.right:
        p2 = print_root_to_node_helper(node.right, value, path)
        
    if p1 or p2:
        return True 
    else:
        path.pop()
        return False  
    


def print_root_to_node(root, value):
    ### we will be using inorder traversal 
    
    path = []
    is_found = print_root_to_node_helper(root, value, path)
    if is_found:
        return path 
    else:
        return -1