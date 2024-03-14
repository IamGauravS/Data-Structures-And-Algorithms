


def two_sum_bst(root, target):
    
    stack_before = []
    stack_after = []
    
    curr = root
    while curr:
        stack_after.append(curr)
        curr = curr.left
        
    curr = root 
    while curr:
        stack_before.append(curr)
        curr = curr.right 
        
    ## current before is from largest to smalles
    ## current after is from smalles to largest 
     
    while stack_after and stack_before:
        right = stack_before[-1]
        left = stack_after[-1]
        if right.data == left.data:
            return None 
        
        if right.data + left.data == target:
            return (right.data, left.data) 
        
        if right.data + left.data < target:
            curr = stack_after.pop()
            curr = curr.right
            while curr:
                
                stack_after.append(curr)
                curr = curr.left
                
        if right.data + left.data > target:
            curr = stack_before.pop()
            curr = curr.left
            while curr:
                
                stack_before.append(curr)
                curr = curr.right
                
    return None 
         