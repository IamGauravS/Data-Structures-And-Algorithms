class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


import queue
class Solution:
     def findMaxiumumDepth(self, root):
          if root is None:
               return 0
          
          return 1 + max(self.findMaxiumumDepth(root.left), self.findMaxiumumDepth(root.right))
     


     def findMaximumDepthIterative(self, root):
          if root is None:
               return 0
          
          nodeQueue = queue.Queue()
          nodeQueue.put([root, 0])
          
          while not nodeQueue.empty():
               currNode, currHeight = nodeQueue.get()

               if currNode.left:
                    nodeQueue.add([currNode.left, currHeight+1])
               if currNode.right:
                    nodeQueue.add([currNode.right, currHeight+1])

          return currHeight + 1
