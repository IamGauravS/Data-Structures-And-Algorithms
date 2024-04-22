class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

import queue

class Solution:
    def topview(self, root):
        if root is None:
            return []

        nodeQueue = queue.Queue()

        levelMap = {}
        nodeQueue.put((root, 0))

        while not nodeQueue.empty():
            size = nodeQueue.qsize()
            for i in range(size):
                curr, height = nodeQueue.get()
                if height not in levelMap:
                    levelMap[height] = curr.val
                if curr.left:
                    nodeQueue.put((curr.left, height-1))
                if curr.right:
                    nodeQueue.put((curr.right, height+1))

        result = []
        for key in sorted(levelMap.keys()):
            result.append(levelMap[key])

        return result
