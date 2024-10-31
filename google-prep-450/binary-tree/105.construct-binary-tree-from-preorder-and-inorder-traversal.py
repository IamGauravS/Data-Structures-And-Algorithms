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
# inorder -> left, root, right
# preorder -> root, left, right

class Solution:
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 or len(inorder) == 0:
            return None 
        
        inorderIndexMap = {}
        for i , val in enumerate(inorder):
            inorderIndexMap[val] = i 

        def buildTreeHelper(preorderStart, preorderEnd, inorderStart, inorderEnd):
            if preorderStart > preorderEnd or inorderStart > inorderEnd:
                return None 
            
            rootVal = preorder[preorderStart]
            root = TreeNode(rootVal)

            inorderIndex = inorderIndexMap[rootVal]

            leftTreeSize = inorderIndex - inorderStart

            root.left = buildTreeHelper(preorderStart+1, preorderStart + leftTreeSize, inorderStart, inorderIndex - 1)
            root.right = buildTreeHelper(preorderStart + leftTreeSize + 1, preorderEnd, inorderIndex + 1, inorderEnd)

            return root 
        
        return buildTreeHelper(0, len(preorder)-1, 0, len(inorder)-1)

        

        

        
        

# @lc code=end

