class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

import queue

class Solution:
    def bottomView(self, root):
        if root is None:
            return []

        nodeQueue = queue.Queue()

        levelMap = {}
        nodeQueue.put((root, 0))

        while not nodeQueue.empty():
            qsize = nodeQueue.qsize()

            for i in range(qsize):
                curr, height = nodeQueue.get()
                levelMap[height] = curr.val

                if curr.left:
                    nodeQueue.put((curr.left, height-1))
                if curr.right:
                    nodeQueue.put((curr.right, height+1))


        bottomView = []
        for key in sorted((levelMap.keys())):
            bottomView.append(nodeQueue[key])

        return bottomView