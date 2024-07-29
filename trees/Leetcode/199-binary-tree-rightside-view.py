# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import queue
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return None 
        
        q = queue.Queue()
        output = []
        
        q.put(root)
        
        while not q.empty():
            qsize = q.qsize()
            temp = []
            for _ in range(qsize):
                curr = q.get()
                temp.append(curr.val)
                if curr.left:
                    q.put(curr.left)
                if curr.right:
                    q.put(curr.right)
                    
            if temp:
                output.append(temp[-1])
                
                
        return output
                
                    
            