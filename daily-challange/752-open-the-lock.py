class Solution:
    def findNoOfWays(self, start, target):
        if start in self.dp:
            return self.dp[start]
        
        if start in self.deadends:
            return float('inf')

        if start == target:
            return 0
        
        isPossible = float('inf')

        for i in range(4):
            if int(start[i]) + 1 <= 9:
                newNumber = start[:i] + str(int(start[i])+1) + start[i+1:]
                isPossible = min(isPossible, self.findNoOfWays(newNumber, target))
            if 0 <= (int(start[i])-1 + 10) % 10 <= 9:
                newNumber = start[:i] + str((int(start[i])-1 + 10) % 10) + start[i+1:]
                isPossible = min(isPossible, self.findNoOfWays(newNumber, target))

        self.dp[start] = isPossible + 1

        
        return self.dp[start]


    def openLock(self, deadends: List[str], target: str) -> int:
        self.dp = {}

        start = "0000"
        self.noOfWays = 0
        self.deadends = deadends
        self.findNoOfWays(start, target)
        return self.dp[start] if self.dp[start] != float('inf') else -1


## bfs is the optimised solution here

from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        queue = deque([('0000', 0)])
        visited = {'0000'}

        while queue:
            node, depth = queue.popleft()
            if node == target:
                return depth
            if node in deadends:
                continue
            for i in range(4):
                for d in (-1, 1):
                    next_node = node[:i] + str((int(node[i]) + d) % 10) + node[i+1:]
                    if next_node not in visited:
                        visited.add(next_node)
                        queue.append((next_node, depth + 1))

        return -1