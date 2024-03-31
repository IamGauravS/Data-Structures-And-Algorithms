# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = queue.Queue()
        q.put(root)
        output = []
        
        while not q.empty():
            lenQueue = q.qsize()
            currLevel = []
            
            for i in range(lenQueue):
                curr = q.get()
                currLevel.append(curr.val)
                if curr.left:
                    q.put(curr.left)
                if curr.right:
                    q.put(curr.right)
            output.append(currLevel) 
            
        return output
        