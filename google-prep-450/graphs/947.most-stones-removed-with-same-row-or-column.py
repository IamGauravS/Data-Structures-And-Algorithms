#
# @lc app=leetcode id=947 lang=python3
#
# [947] Most Stones Removed with Same Row or Column
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
                self.parent[root1] = root2
                self.rank[root2] += 1  


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        """
            This function implements the functionality to remove maximum 
            number of stones that either share the same row or the same
            column as another stone. It uses disjoint set to achieve this where
            a stone sharing same row or column are assumed to be connected

            Args:
            stones (List[List[int]]) : i, j coordinates of the stone

            Returns:
            stonesRemoved (int) : stones that can be removed
        """

        ## if there are only 1 or 0 stones then we don't need to remove anything
        if len(stones) < 2:
            return 0
        
        uf = UnionFind()
        
        ## create disjoint set
        for x, y in stones:
            uf.union(x, y + 100000) 

        ## number of disjoint sets
        uniqueSets = {uf.find(x) for x, y in stones} | {uf.find(y + 100000) for x, y in stones}

        ## number of stones that can be removed is equal to total no of stones - no of disjoint set

        stonesRemoved = len(stones) - len(uniqueSets)
        return stonesRemoved


        
# @lc code=end

