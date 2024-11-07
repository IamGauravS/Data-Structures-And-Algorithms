#
# @lc app=leetcode id=305 lang=python3
#
# [305] Number of Islands II
#

# @lc code=start

from collections import defaultdict

class UnionFind:
    """
    Implements Union-Find with path compression and union by rank.
    """

    def __init__(self):
        self.parent = defaultdict(lambda: None)  # Corrected lambda syntax
        self.rank = defaultdict(int)

    def find(self, node: int) -> int:
        """
        Finds and returns the root of the given node, applying path compression.

        Args:
            node (int): The node whose root is to be found.
            
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
        Unites two nodes by their rank, attaching the smaller tree under the larger one.

        Args:
            node1 (int): The first node to union.
            node2 (int): The second node to union.
            
        Returns:
            None
        """
        root1 = self.find(node1)
        root2 = self.find(node2)

        # Only unite if they have different roots
        if root1 != root2:
            # Union by rank
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root2] > self.rank[root1]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1  

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        """
            This function return a list of integers representing number of islands
            at each step. It uses unionfind to achieve that and joins all the neighboring 
            islands present to make 1 island

            Args:
                m (int) : no of rows in grid 
                n (int) : no of cols in grid
                positions (List[List[int]]) : position of land in a grid

            Returns:
                islandsAfterEachStep (int) : no of islands after marking a position in
                grid as 1
        """

        ## check for edge cases
        if m == 0 and n == 0:
            return []
        if not positions:
            return []
        
        islandsAfterEachStep = []
        uf = UnionFind()
        delta = [(0,1), (1,0), (0,-1), (-1,0)]  ## 4 ways movement
        landCordinates = set() ## set to store land cordinate

        for position in positions:
            curri, currj = position[0], position[1]

            ## check for duplicates
            if (curri, currj) not in landCordinates:
                landCordinates.add((curri, currj))
                uf.parent[curri+100000*currj] = curri+100000*currj  ## we multiple by 10^5 to create a unique key

                noOfConnectedLands = 0  ## count unique islands nearby

                ## iterate over neighbours
                for dx, dy in delta:
                    newi = curri + dx 
                    newj = currj + dy 
                    
                    
                    if 0 <= newi < m and 0 <= newj < n:  ## check for out of bounds condition
                        if (newi, newj) in landCordinates:
                            if uf.find(curri+100000*currj) != uf.find(newi+100000*newj):
                                noOfConnectedLands += 1
                                uf.union(curri+100000*currj, newi+100000*newj)

                ## if there no connected land then we added a new island
                if noOfConnectedLands == 0:
                    if not islandsAfterEachStep:
                        islandsAfterEachStep.append(1)
                    else:
                        islandsAfterEachStep.append(islandsAfterEachStep[-1] + 1)

                ## if there are connected lands then we need to decrease or keep same the number of land
                else:
                    islandsAfterEachStep.append(islandsAfterEachStep[-1] - (noOfConnectedLands-1))

            ## if there is a duplicate then we just add the last number of island again
            else:
                islandsAfterEachStep.append(islandsAfterEachStep[-1])
                


        return islandsAfterEachStep



        
# @lc code=end

