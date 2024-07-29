

def find_kth_smallest_element_helper(root, k, output):
    if root is None:
        return 
    if len(output) ==k:
        return 
    
    find_kth_smallest_element_helper(root.left, k, output)
    output.append(root.data)
    find_kth_smallest_element_helper(root.right, k, output)
    return 

def find_kth_smallest_element(root, k):
    ## do inorder traversal we will get sorted array then take the kth value 
    output = []
    find_kth_smallest_element_helper(root, k,  output)
    return output[k-1] if len(output) >= k else None 