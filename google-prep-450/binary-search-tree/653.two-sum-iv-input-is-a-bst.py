#
# @lc app=leetcode id=653 lang=python3
#
# [653] Two Sum IV - Input is a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """
        Two-pointer kind of solution based on generators
        Time: O(n)
        Space: O(h) where h is the height of the tree 
               Can be as good as O(logn) if tree is balanced
        """
        if root.left is None and root.right is None:
            return False  # Only one element in a tree
        
        def ascending(node: TreeNode):
            """ Generates values in ascending order """
            if node:
                yield from ascending(node.left)
                yield node.val
                yield from ascending(node.right)
        
        def descending(node: TreeNode):
            """ Generates values in descending order """
            if node:
                yield from descending(node.right)
                yield node.val
                yield from descending(node.left)

        lo = ascending(root)   # Lower "pointer" generator
        loval = next(lo)       # Smallest value in a BST
        hi = descending(root)  # higher "pointer" generator
        hival = next(hi)       # Greatest value in a BST
        while loval < hival:
            sumval = loval + hival
            if sumval == k:
                return True
            if sumval < k:
                loval = next(lo)
            if k < sumval:
                hival = next(hi)
        return False
        
# @lc code=end

