#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# inorder -> left root right
# postorder -> left right root
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0 or len(postorder) == 0:
            return None 
        
        inorderIdxMap = {}
        for i, val in enumerate(inorder):
            inorderIdxMap[val] = i 

        def buildTreeHelper(inorderStart, inorderEnd, postorderStart, postorderEnd):
            if inorderStart > inorderEnd or postorderStart > postorderEnd:
                return None 
            
            rootVal = postorder[postorderEnd]
            root = TreeNode(rootVal)

            idx = inorderIdxMap[rootVal]
            leftTreelen = idx - inorderStart

            root.left = buildTreeHelper(inorderStart, idx - 1, postorderStart, postorderStart+leftTreelen-1)
            root.right = buildTreeHelper(idx +1, inorderEnd, postorderStart+leftTreelen , postorderEnd - 1)

            return root 
        
        return buildTreeHelper(0, len(inorder)-1, 0, len(postorder)-1)
        

        
# @lc code=end

