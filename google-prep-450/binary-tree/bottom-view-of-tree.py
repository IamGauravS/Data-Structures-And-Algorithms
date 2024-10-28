from collections import deque, defaultdict
class Solution:
    def bottomView(self, root):
        # code here

        if root is None:
            return []
            
        heightDict = defaultdict(int)
        queue = deque([(root, 0)])
        
        while queue:
            currNode, height = queue.popleft()
            
            heightDict[height] = currNode.data
            
            if currNode.left:
                queue.append((currNode.left, height-1))
                
            if currNode.right:
                queue.append((currNode.right, height+1))
                
        sortedHeight = sorted(heightDict.keys())
        output = []
        for height in sortedHeight:
            output.append(heightDict[height])
            
        return output