#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Function to compute the height of the leftmost and rightmost paths
        def get_height(node, go_left):
            height = 0
            while node:
                height += 1
                node = node.left if go_left else node.right
            return height
        
        # Get heights of leftmost and rightmost paths
        left_height = get_height(root, True)
        right_height = get_height(root, False)
        
        # If left and right heights are the same, it's a full complete binary tree
        if left_height == right_height:
            return (1 << left_height) - 1  # 2^height - 1
        
        # Otherwise, recursively count nodes in left and right subtrees
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

        
# @lc code=end

