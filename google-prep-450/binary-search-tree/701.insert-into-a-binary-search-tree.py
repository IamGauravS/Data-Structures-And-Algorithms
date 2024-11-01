#
# @lc app=leetcode id=701 lang=python3
#
# [701] Insert into a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if root == None:
            return TreeNode(val)

        curr = root 
        prev = root 

        while curr:
            if val < curr.val:
                prev = curr 
                curr = curr.left 
            else:
                prev = curr 
                curr = curr.right 

        node = TreeNode(val)

        if val > prev.val:
            prev.right = node 
        else:
            prev.left = node 

        return root
        
# @lc code=end

