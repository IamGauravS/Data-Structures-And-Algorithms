# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import queue
class Solution:
    def addLeftBoundry(self, root):
        curr = root.left

        while curr:
            if not (curr.left == None and curr.right == None):
                self.left.append(curr.val)

            if curr.left:
                curr = curr.left
            else:
                curr = curr.right

        return

    def addRightBoundry(self, root):
        curr = root.right

        while curr:
            if not (curr.left == None and curr.right == None):
                self.right.append(curr.val)

            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        return

    def addLeaves(self, root):
        if root.left == None and root.right == None:
            self.leaf.append(root.val)
            return 
        
        if root.left:
            self.addLeaves(root.left)
        if root.right:
            self.addLeaves(root.right)

        return 


    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        self.result = []
        self.left= []
        self.right = []
        self.leaf = []

        self.addLeftBoundry(root)
        self.addRightBoundry(root)
        self.addLeaves(root)

        if not (root.left == None and root.right == None):
            self.result.append(root.val)

        self.result = self.result + self.left + self.leaf + self.right[::-1]
        return self.result

        
                    

        