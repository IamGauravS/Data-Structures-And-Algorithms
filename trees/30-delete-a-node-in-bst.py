

def delete_node(root, value):
    if root is None:
        return root 
    if value < root.data:
        root.left = delete_node(root.left, value)
    if value > root.data:
        root.right = delete_node(root.right, value)
        
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp 
        if root.right is None:
            temp = root.right
            root = None 
            return temp 
        
        temp = minValueNode(root.right)
        root.data = temp.data
        root.right = delete_node(root.right, temp.data)
        
    return root 



def minValueNode(node):
    current = node 
    while(current.left is not None):
        current = current.left 
        
    return current 
        
    