
import sys.maxsize
## find greatest value smaller then or equal to key
def find_floor(root, key):
    floor = sys.maxsize
    
    while root:
        if root.data == key:
            floor = root.data
            return floor 
        
        elif root.data < key:
            floor = root.data 
            root = root.right 
            
        else:
            root = root.left 
            
    return floor 