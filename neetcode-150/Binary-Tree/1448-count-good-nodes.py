# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _goodNodesHelper(self, root, path):
        if root is None:
            return 0
        
        if len(path) == 0 or path[-1] <= root.val:
            return 1 + self._goodNodesHelper(root.left, path + [root.val]) + self._goodNodesHelper(root.right, path + [root.val])
        
        else:
            if path[-1] > root.val:
                return self._goodNodesHelper(root.left, path) + self._goodNodesHelper(root.right, path)
        
            
    def goodNodes(self, root: TreeNode) -> int:
        path = []
        
        return self._goodNodesHelper(root, path)
        