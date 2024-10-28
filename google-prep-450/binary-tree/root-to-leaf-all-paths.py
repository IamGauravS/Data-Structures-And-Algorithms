class Solution:
    def __init__(self):
        self.allPaths = []
        
    def pathsHelper(self, root, currPath):
        if root is None:
            return 
        
        currPath.append(root.data)
        
        if not root.left and not root.right:
            self.allPaths.append(currPath[::])
            
        if root.left:
            self.pathsHelper(root.left, currPath)
        if root.right:
            self.pathsHelper(root.right, currPath)
            
        currPath.pop()
        return 
    
    def Paths(self, root : Optional['Node']) -> List[List[int]]:
        # code here
        
        self.pathsHelper(root, [])
        return self.allPaths
    

from collections import deque

class Solution:
    def Paths(self, root: Optional['Node']) -> List[List[int]]:
        if root is None:
            return []
        
        result = []
        queue = deque([(root, [root.data])])  # Each element is (node, path)

        while queue:
            node, path = queue.popleft()
            
            # If it's a leaf node, add the path to result
            if not node.left and not node.right:
                result.append(path)
            
            # Enqueue left and right children with updated paths
            if node.left:
                queue.append((node.left, path + [node.left.data]))
            if node.right:
                queue.append((node.right, path + [node.right.data]))
        
        return result


class Solution:
    def Paths(self, root: Optional['Node']) -> List[List[int]]:
        result = []
        
        def preorder(node, path):
            if node is None:
                return
            
            path.append(node.data)
            
            if not node.left and not node.right:
                result.append(path[:])
            
            preorder(node.left, path)
            preorder(node.right, path)
            
            path.pop()
        
        preorder(root, [])
        return result
