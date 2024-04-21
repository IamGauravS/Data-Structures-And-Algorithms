import queue

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodeQueue = queue.Queue()

        heightSet = {}

        nodeQueue.put((root, 0, 0))  # Add depth to the queue

        while not nodeQueue.empty():
            currNode, height, depth = nodeQueue.get()

            if height not in heightSet:
                heightSet[height] = []

            # Add depth to each node's information
            heightSet[height].append((depth, currNode.val))

            if currNode.left:
                nodeQueue.put((currNode.left, height-1, depth+1))  # Increment depth
            if currNode.right:
                nodeQueue.put((currNode.right, height+1, depth+1))  # Increment depth

        sortedHeights = sorted(heightSet.keys())

        result = []
        for height in sortedHeights:
            # Sort the nodes at each height by depth and value
            nodes = sorted(heightSet[height])
            # Extract the node values
            result.append([val for _, val in nodes])

        return result


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import queue

class Solution:
        def helper(self, placement,level, root, dic):
            if(not root):
                return
            dic[placement].append((level, root.val))
            self.helper(placement-1, level+1, root.left, dic)
            self.helper(placement+1, level+1, root.right, dic)
		
        def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
            dic = defaultdict(list)
            self.helper(0,0, root, dic)
            result = []
            for i in sorted(dic.keys()):
                temp = []
                for j in sorted(dic[i]):
                    temp.append(j[1])
                result.append(temp)
            return result