
def is_symatric_helper(left, right):
    if left == right == None:
        return True
    if (left == None and right != None) or (right == None and left != None) or (right.data != left.data):
        return False
    
    side1 = is_symatric_helper(left.left, right.right)
    side2 = is_symatric_helper(left.right, right.left)
    
    return side1 and side2 
    
    


def is_symmatric_tree(root):
    if root is None:
        return True 
    
    return is_symatric_helper(root.left, root.right)