



def flatten_binary_tree(root):
    
    stack = []
    stack.push(root)
    
    while stack:
        curr = stack.pop()
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
            
        if len(stack) > 0:
            curr.right = stack[-1]
            
        curr.left = None
        
    return root 