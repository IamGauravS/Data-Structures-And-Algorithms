#
# @lc app=leetcode id=827 lang=python3
#
# [827] Making A Large Island
#

# @lc code=start
from collections import defaultdict

class UnionFind:
    """
    Implements Union-Find with path compression and union by size.
    """

    def __init__(self) -> None:
        self.parent = defaultdict(lambda: None)
        self.size = defaultdict(lambda: 1)  # Initialize size to 1 for each new node

    def find(self, node: int) -> int:
        """
        Finds and returns the root of the node, with path compression applied.

        Args:
            node (int): Node for which to find the root.

        Returns:
            int: The root of the node.
        """
        # Initialize the parent if the node is new
        if self.parent[node] is None:
            self.parent[node] = node

        # Apply path compression
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])

        return self.parent[node]
    
    def union(self, node1: int, node2: int) -> None:
        """
        Unites two nodes by their size, attaching the smaller tree under the larger.

        Args:
            node1 (int): The first node to unite.
            node2 (int): The second node to unite.
            
        Returns:
            None
        """
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            # Union by size
            if self.size[root1] > self.size[root2]:
                self.parent[root2] = root1
                self.size[root1] += self.size[root2]
            else:
                self.parent[root1] = root2
                self.size[root2] += self.size[root1]

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        """
            This functions returns the coordinate where we must change 
            a 0 to 1 to form the largest island. It first tracks all the islands
            using the union find and then later uses their size to find the correct location

            Args:
                grid List[List[int]] : a grid containing all the islands

            Returns:
                maxIslandSize (int) : largest island that can be formed after changing 0 to 1
        """

        uf = UnionFind()
        nrows = len(grid)
        ncols = len(grid[0])

        if not nrows or not ncols:
            return 0

        ## store the islands
        delta = [(0,1), (1,0), (0,-1), (-1,0)]
        maxIslandSize = 1  ## we initialise this as 1 because we can change any cell with value 0 to 1 if there are no islands in grid
        
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == 1:
                    ## iterate over the neighbors and combine them to form islands
                    for dx, dy in delta:
                        newi = i + dx 
                        newj = j + dy 
                        if 0 <= newi < nrows and 0 <= newj < ncols and grid[newi][newj] == 1:
                            root1 = uf.find(i + 1000*j)
                            root2 = uf.find(newi + 1000*newj)
                            if root1 != root2:
                                uf.union(i + 1000*j, newi + 1000*newj)
                                


        ## find the optimal place for replacing 0 with 1
        ## this block of code goes through all the zeros and finds the max
        ## island that it can form

        
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == 0:
                    ## a set containing roots of all the unique islands surrounding that cell
                    uniqueIslands = set()

                    for dx, dy in delta:
                        newi = i + dx 
                        newj = j + dy 
                        if 0 <= newi < nrows and 0 <= newj < ncols and grid[newi][newj] == 1:
                            uniqueIslands.add(uf.find(newi+1000*newj))

                    ## atleast 1 island was found in neighbourhood
                    if uniqueIslands:
                        newIslandSize = 0
                        for island in uniqueIslands:
                            newIslandSize += uf.size[island]

                        maxIslandSize = max(maxIslandSize, newIslandSize+1)

                if grid[i][j] == 1:
                    maxIslandSize = max(maxIslandSize, uf.size[i + 1000*j])



        return maxIslandSize
                        

        
# @lc code=end

