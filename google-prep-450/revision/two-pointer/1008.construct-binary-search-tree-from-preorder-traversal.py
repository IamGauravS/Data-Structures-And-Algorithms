#
# @lc app=leetcode id=1008 lang=python3
#
# [1008] Construct Binary Search Tree from Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        # Helper function to construct BST within bounds
        def helper(lower, upper):
            nonlocal idx
            if idx == len(preorder):  # If all nodes are processed
                return None

            val = preorder[idx]
            # If the current value is out of bounds, it doesn't belong to this subtree
            if val < lower or val > upper:
                return None

            # Move to the next node
            idx += 1
            # Create the root node
            root = TreeNode(val)
            # Build the left and right subtrees with updated bounds
            root.left = helper(lower, val)  # Left subtree: values < val
            root.right = helper(val, upper)  # Right subtree: values > val
            return root

        idx = 0
        return helper(float('-inf'), float('inf'))

        
# @lc code=end

