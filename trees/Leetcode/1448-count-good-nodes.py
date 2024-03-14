# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        path = []
        count = 0
        count = self.countgoodnodes(root, path, count)
        
        return count 
    
    def countgoodnodes(self, root, path, count):
        if root is None:
            return count 
        
        if len(path) == 0 or all(root.val >= x for x in path):
            count += 1
            
        path.append(root.val)
        
        count = self.countgoodnodes(root.right, path, count)
        
    
        count = self.countgoodnodes(root.left, path, count)
            
        path.pop()
            
        return count
    
    
    
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.countgoodnodes(root, float('-inf'))
    
    def countgoodnodes(self, root, max_val):
        if root is None:
            return 0 
        
        count = 0
        if root.val >= max_val:
            count += 1
            max_val = root.val
            
        count += self.countgoodnodes(root.right, max_val)
        count += self.countgoodnodes(root.left, max_val)
        
        return count