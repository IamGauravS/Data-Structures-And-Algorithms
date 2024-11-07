#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
            This function merges account with common emails to same name.
            It uses disjoint function to achiever this

            Args:
                accounts (List[List[str]]) : a list of list with each list containing name, email1 , email2, ..

            Returns:
                mergedAccounts (List[List[str]]) : a list of list with each list containing name, and all the merged emails
        """

        if not accounts:
            return []
        
        uf = UnionFind()

        ## create email to name mapping and run union find in the same loop
        emailToNameMap = {}
        
        for i in range(len(accounts)):
            name = accounts[i][0]
            firstEmail = accounts[i][1]
            for email in accounts[i][1:]:
                emailToNameMap[email] = name 
                uf.union(firstEmail, email)


        ## group emails together if they have common root
        emailGroups = defaultdict(list)
        for email in uf.parent:
            root = uf.find(email)
            emailGroups[root].append(email)

        mergedAccounts = []
        for key, value in emailGroups.items():
            name = emailToNameMap[value[0]]
            mergedAccounts.append([name] + sorted(value))


        return mergedAccounts

        
# @lc code=end

