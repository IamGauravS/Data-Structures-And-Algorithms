# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkIfSymmetric(self, leftNode, rightNode):
        if leftNode == None and rightNode == None:
            return True
        if leftNode == None or rightNode == None:
            return False 
        if leftNode.val != rightNode.val:
            return False 

        return self.checkIfSymmetric(leftNode.right, rightNode.left) and self.checkIfSymmetric(leftNode.left, rightNode.right)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True 

        return self.checkIfSymmetric(root.left, root.right)

