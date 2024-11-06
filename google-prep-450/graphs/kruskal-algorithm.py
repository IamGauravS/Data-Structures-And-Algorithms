from collections import defaultdict
from typing import List, Tuple
class UnionFind:
    """

        This class implements the union find by rank algorithm

    """

    def __init__(self) -> None:
        self.rank = defaultdict(int)
        self.parent = defaultdict(lambda : None)

    def find(self, node : int) -> int:
        """
            This function returns the root of a node
            and does path compression

            Args:

            node (int) : node for which we want to find the root

            Returns:

            root (int) : root of the node
        """

        ## if node doesn't exsis in the graph
        if self.parent[node] == None:
            self.parent[node] = node 

        ## apply path compression
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])

        ##return root
        return self.parent[node]
    

    def union(self, node1 : int, node2 : int) -> None:
        """
        
        This function does a union by rank of two nodes attaching
        the smaller node under the bigger node

        Args:
            node1 (int) : first node
            node2 (int) : second node

        Returns:

            None

        """

        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            ## join the smaller tree under the bigger tree
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1 
            elif self.rank[root2] > self.rank[root1]:
                self.parent[root1] = root2 
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

        return 
    
class Solution:
    def kruskalAlgorithm(self, n : int, edges : List[Tuple[int, int, int]]) -> int:
        """
            This function implements kruskals algorithm which sorts
            the edges by weight and then creates a mst by using union find

            Args:
                n: number of nodes
                edges: edges containing (source, destination, weight)

            Returns:
                mstWeight (int) : total weight of minimum spanning tree
        """

        ## return if edges is empty
        if not edges:
            return 0
        
        ## sort the edges by weight
        edges.sort(key = lambda x: x[2])

        mstEdges = [] # store minimum spanning tree
        mstWeight = 0
        uf = UnionFind()

        ## implement kruskal algo
        for source, destination, weight in edges:
            if uf.find(source) != uf.find(destination): ## if roots are not euqal
                mstWeight += weight
                mstEdges.append((source, destination))
                uf.union(source, destination)

            ## stop if we have enough edges
            if len(mstEdges) == n-1:
                break

        ## check if we actually have an mst
        if len(mstEdges) != n-1:
            return -1
        
        return mstWeight





    