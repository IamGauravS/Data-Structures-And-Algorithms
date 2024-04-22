from queue import Queue

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        nodeQueue = Queue()
        nodeQueue.put((root, 1))
        maxWidth = 0

        while not nodeQueue.empty():
            qsize = nodeQueue.qsize()
            currLevel = []
            for _ in range(qsize):
                currNode, position = nodeQueue.get()
                currLevel.append(position)
                if currNode.left:
                    nodeQueue.put((currNode.left, position * 2))
                if currNode.right:
                    nodeQueue.put((currNode.right, position * 2 + 1))

            maxWidth = max(maxWidth, currLevel[-1] - currLevel[0] + 1)

        return maxWidth