class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findPath(self, root, node):
        if root == None:
            return False

        if root.val == node.val:
            self.path.append(node.val)
            return True

        self.path.append(root.val)
        if self.findPath(root.left, node):
            return True
        elif self.findPath(root.right, node):
            return True
        self.path.pop()

        return False
         
        
    def findPathToNode(self, root: Optional[TreeNode], node: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        self.path = []
        self.findPath(root, node)

        return self.path if self.path != [] else -1