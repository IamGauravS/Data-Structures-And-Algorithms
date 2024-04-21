class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def checkIfTreeIsBalancedHelper(self, root):
        if root is None or self.check[0] == False:
            return 0

        lHeight = 0
        rHeight = 0

        if root.left:
            lHeight = self.checkIfTreeIsBalancedHelper(root.left)

        if root.right:
            rHeight = self.checkIfTreeIsBalancedHelper(root.right)

        if abs(lHeight - rHeight) > 1:
            self.check[0] = False

        return 1 + max(lHeight, rHeight)
    
    def checkIfTreeIsBalanced(self, root):
        if root is None:
            return True
        self.check = [True]

        self.checkIfTreeIsBalancedHelper(root)
        return self.check[0]