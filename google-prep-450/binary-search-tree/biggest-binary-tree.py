class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        # Helper function to recursively determine if a subtree is a BST
        def helper(node):
            if not node:
                return (True, 0, float('inf'), float('-inf'))
            
            left_is_bst, left_size, left_min, left_max = helper(node.left)
            right_is_bst, right_size, right_min, right_max = helper(node.right)
            
            # Check if current node is a valid BST root
            if left_is_bst and right_is_bst and left_max < node.val < right_min:
                size = left_size + right_size + 1
                min_val = min(left_min, node.val)
                max_val = max(right_max, node.val)
                return (True, size, min_val, max_val)
            else:
                # If not a BST, return the size of the largest BST found in the subtrees
                return (False, max(left_size, right_size), 0, 0)

        # Start recursion from the root and return the largest BST size
        return helper(root)[1]
