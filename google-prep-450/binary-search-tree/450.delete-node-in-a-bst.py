#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root 
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        else:
            ## case 1. if it is a leaf node
            if not root.left and not root.right:
                root = None 

            ## case 2. if it has one node
            elif not root.left:
                root = root.right 
            elif not root.right:
                root = root.left 

            else:
            ## case 3. if it has two nodes
                successor = self.findMin(root.right)
                root.val = successor.val
                ## delete the successor node
                root.right = self.deleteNode(root.right, successor.val)

        return root 
    
    def findMin(self, node):
        current = node 
        while current.left:
            current = current.left 

        return current 
            
        
# @lc code=end

