

def recover_bst(root):
    
    def inorder(root, output):
        if root is None:
            return 
        if root.left:
            inorder(root.left, output)
        output.append(root.data)
        if root.right:
            inorder(root.right, output)
            
    output = []
    inorder(root, output)
    
    first = None 
    mid = None 
    last = None 
    
    for i in range(1, len(output)):
        if output[i].data < output[i-1].data:
            if first is None:
                first = output[i-1]
                mid = output[i]
            else:
                last = output[i]

    if last is None:  # two swapped nodes are adjacent
        first.data, mid.data = mid.data, first.data
    else:  # two swapped nodes are not adjacent
        first.data, last.data = last.data, first.data