#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []
        
        output = []
        nodeStore = deque()

        nodeStore.append(root)

        while nodeStore:
            temp = []
            noOfNodes = len(nodeStore)

            for i in range(noOfNodes):
                currNode = nodeStore.popleft()
                temp.append(currNode.val)
                if currNode.left:
                    nodeStore.append(currNode.left)
                if currNode.right:
                    nodeStore.append(currNode.right)

            output.append(temp)

        return output
            
# @lc code=end

## in a different way

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        output, queue = [], deque([root])

        while queue:
            level_values = [node.val for node in queue]
            output.append(level_values)

            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return output
