class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def childrenSum(self, root, node):
        if root == None:
            return root

        child = 0

        if root.left:
            child += root.left.val
        if root.right:
            child += root.right.val


        if child >= root.val:
            root.val = child 

        else:
            if root.left:
                root.left.val = root.val
            if root.rightL:
                root.right.val = root.val


        self.changeTree(root.left)
        self.changeTree(root.right)

        tot = 0

        if root.left:
            tot+= root.left.val
        if root.right:
            tot+= root.right.val


        if root.left or root.right:
            root.val = tot

        return