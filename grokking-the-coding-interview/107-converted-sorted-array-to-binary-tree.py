# Definition of a binary tree node
#
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

from ds_v1.BinaryTree.BinaryTree import TreeNode

def sorted_array_to_bst(nums):
    
    # Replace this placeholder return statement with your code
    
    if not nums:
        return None 
    
    low = 0
    high = len(nums)
    
    
    mid = (low+high)//2
    
    root = TreeNode(nums[mid])
    
    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid+1:])
    
    return root