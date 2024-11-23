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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 or len(inorder) == 0:
            return None 
        
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}

        def helper(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int) -> Optional[TreeNode]:
            if preorder_left > preorder_right:
                return None
            
            # The first element in the preorder list is the root
            root_val = preorder[preorder_left]
            root = TreeNode(root_val)
            
            # Get the index of the root in the inorder list
            inorder_root_index = inorder_index_map[root_val]
            
            # Calculate the number of elements in the left subtree
            left_subtree_size = inorder_root_index - inorder_left
            
            # Recursively build the left and right subtrees
            root.left = helper(preorder_left + 1, preorder_left + left_subtree_size, inorder_left, inorder_root_index - 1)
            root.right = helper(preorder_left + left_subtree_size + 1, preorder_right, inorder_root_index + 1, inorder_right)
            
            return root
        
        return helper(0, len(preorder)-1, 0, len(inorder)-1)
        
# @lc code=end

