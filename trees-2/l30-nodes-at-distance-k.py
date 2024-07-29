# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


import queue
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        self.parent = {}

        self.parent[root] = -1

        stack = []
        stack.append(root)

        while stack:
            curr = stack.pop()

            if curr.left:
                self.parent[curr.left] = curr
                stack.append(curr.left)
            if curr.right:
                self.parent[curr.right] = curr
                stack.append(curr.right)


        ### do bfs 
        nodeQueue = queue.Queue()
        nodeQueue.put((target, 0, None))
        resultNodes = []


        while not nodeQueue.empty():
            currNode, dest, parent = nodeQueue.get()

            if dest == k:
                resultNodes.append(currNode.val)
            else:
                if currNode.left and currNode.left != parent:
                    nodeQueue.put((currNode.left, dest+1, currNode))
                if currNode.right and currNode.right != parent:
                    nodeQueue.put((currNode.right, dest+1, currNode))
                if self.parent[currNode] != -1 and self.parent[currNode] != parent:
                    nodeQueue.put((self.parent[currNode], dest+1, currNode))


        return resultNodes