#
# @lc app=leetcode id=1319 lang=python3
#
# [1319] Number of Operations to Make Network Connected
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
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        """
            This function return minimum number of cable changes required
            to make all the computers connected. It used disjoin union set
            to find unconnected networks and then returns the connections required
            to connect them

            Args:
                n (int) : number of computers
                connections (List[List(int)]) : connections

            Returns :
                connectionChanges (int) : number of connection changes required
        """

        ## if there are only 1 or 2 computers then we dont need to connect anything
        if n < 2:
            return 0
        
        ## if there are fewwer connections than n-1 then we cant make new connections
        ## and the graph is disconnected
        if len(connections) < n-1:
            return -1
        
        uf = UnionFind()

        ## create sets of connected computers
        for comp1, comp2 in connections:
            if uf.find(comp1) != uf.find(comp2):
                uf.union(comp1, comp2)

        ## get unique disjoint networks
        networks = set()
        for comp in range(n):
            networks.add(uf.find(comp))

        ## no of new connections required will be total number of disjoint networks -1
        connRequired = len(networks) - 1
        
        return connRequired

        



        
# @lc code=end

