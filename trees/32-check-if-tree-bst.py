

def check_if_bt_helper(root, left_range, right_range):
    if root is None:
        return True 
    
    if root.data > right_range or root.data < left_range:
        return False 
    
    check_left = check_if_bt_helper(root.left, left_range, root.data)
    check_right = check_if_bt_helper(root.right, root.data, right_range)
    
    return check_left and check_right
                
            
import sys 

def check_if_bt(root):
    if root is None:
        return True 
        
    left_range = -sys.maxsize
    right_range = sys.maxsize
    
    return check_if_bt_helper(root, left_range, right_range)