#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTreeHelper(self, preorderStart, preorderEnd, inorderStart, inorderEnd):
        if preorderStart >= preorderEnd or inorderStart >= inorderEnd:
            return None

        root = TreeNode(self.preorder[preorderStart])
        inorderidx = self.numToPosMap[self.preorder[preorderStart]]

        lenPreorder = inorderidx - inorderStart + 1

        root.left = self.buildTreeHelper(preorderStart+1, preorderStart + lenPreorder  ,inorderStart, inorderidx)
        root.right = self.buildTreeHelper(preorderStart+lenPreorder, preorderEnd, inorderidx+1, inorderEnd)
        return root


    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 or len(inorder) == 0:
            return None 

        self.preorder = preorder

        self.numToPosMap = {}
        for i in range(len(inorder)):
            self.numToPosMap[inorder[i]] = i
        return self.buildTreeHelper(0, len(preorder), 0 , len(inorder))
        
        
# @lc code=end

