# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import queue
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        result = []
        nodeQueue = queue.Queue()

        nodeQueue.put(root)
        flag = True

        while not nodeQueue.empty():
            temp = []
            qsize = nodeQueue.qsize()

            for i in range(qsize):
                curr = nodeQueue.get()
                temp.append(curr.val)
                if curr.left:
                    nodeQueue.put(curr.left)
                if curr.right:
                    nodeQueue.put(curr.right)


            if flag:
                result.append(temp[:])
                flag = False

            else:
                result.append(temp[::-1])
                flag = True


        return result

            

