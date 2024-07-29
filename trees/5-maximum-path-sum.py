def find_maximum_path_sum(root):
    def find_max_path(root, maxi):
        if root == None:
            return 0 
        
        left = max(0, find_max_path(root.left, maxi))
        right = max(0, find_max_path(root.right, maxi))
        
        sum_till_now = root.data + left + right 
        maxi[0] = max(maxi[0], sum_till_now)
        
        return root.data + max(left, right)
    
    
    maxi = [float('-inf')]
    find_max_path(root, maxi)
    return maxi[0]