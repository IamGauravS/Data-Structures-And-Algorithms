#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        def postorderTraversalHelper(node):
            if node == None:
                return 
            
            postorderTraversalHelper(node.left)
            postorderTraversalHelper(node.right)
            output.append(node.val)

        postorderTraversalHelper(root)
        return output
        
# @lc code=end


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        output = []
        stack1, stack2 = [root], []

        while stack1:
            currNode = stack1.pop()
            stack2.append(currNode)

            if currNode.left:
                stack1.append(currNode.left)
            if currNode.right:
                stack1.append(currNode.right)


        while stack2:
            output.append(stack2.pop().val)

        return output
    

## using 1 stack

def postorder_traversal(root):
    if not root:
        return []

    stack, result = [], []
    current = root
    last_visited = None

    while stack or current:
        # Traverse to the leftmost node
        if current:
            stack.append(current)
            current = current.left
        else:
            # Peek the node from the stack
            node = stack[-1]

            # If there is a right child and it hasn't been visited yet, traverse the right subtree
            if node.right and last_visited != node.right:
                current = node.right
            else:
                # Visit the node if there's no right child or right has already been visited
                result.append(node.val)
                last_visited = stack.pop()

    return result
