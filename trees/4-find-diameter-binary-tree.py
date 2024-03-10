## longest path betwee any two nodes
## doesnt need to pass through root 

def find_max_diameter(root):
    def find_max(node, maxi):
        if node is None:
            return 0
        lh = find_max(node.left, maxi)
        rh = find_max(node.right, maxi)
        
        maxi[0] = max(maxi[0], rh+lh)
        return 1 + max(lh, rh)
    
    maxi = [0]
    find_max(root, maxi)
    return maxi[0]