class Solution:
    def findHeight(self, root, parent):
        if root == None:
            return 0
        currHeight = 0
        for node in self.adjList[root]:
            if node != parent:
                currHeight = max(currHeight, self.findHeight(node, root))

        return 1 + currHeight
        
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if len(edges) == 0:
            if n == 1:
                return [0]
            if n == 0:
                return []
        self.adjList = {}

        for edge in edges:
            src, dest = edge 
            if src not in self.adjList:
                self.adjList[src] = []
            if dest not in self.adjList:
                self.adjList[dest] = []

            self.adjList[src].append(dest)
            self.adjList[dest].append(src)


        minHeight = float('inf')
        minHeightNodes = []

        for i in range(n):
            
            currHeight = self.findHeight(i, -1)
            if currHeight == minHeight:
                minHeightNodes.append(i)
            if currHeight < minHeight:
                minHeight = currHeight
                minHeightNodes = []
                minHeightNodes.append(i)


        return minHeightNodes