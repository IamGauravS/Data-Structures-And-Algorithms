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
        nodeQueue = deque()
        nodeQueue.append((target, 0))
        time = 0
        seen = set()
        seen.add(target)
        while nodeQueue:
            currNode, currTime = nodeQueue.popleft()

            time = max(currTime, time)

            if currNode.left and currNode.left not in seen:
                nodeQueue.append((currNode.left, currTime+1))
                seen.add(currNode.left)
            
            if currNode.right and currNode.right not in seen:
                nodeQueue.append((currNode.right, currTime+1))
                seen.add(currNode.right)

            if currNode in self.parent and self.parent[currNode] not in seen:
                nodeQueue.append((self.parent[currNode], currTime+1))
                seen.add(self.parent[currNode])

        return time
