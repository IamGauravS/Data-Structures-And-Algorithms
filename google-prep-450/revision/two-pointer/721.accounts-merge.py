#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#

# @lc code=start
from collections import defaultdict
from typing import List

class UnionFind:
    def __init__(self):
        self.parent = defaultdict(lambda: None)
        self.rank = defaultdict(int)

    def find(self, node):
        if self.parent[node] is None:
            self.parent[node] = node 

        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])

        return self.parent[node]
    
    def union(self, node1, node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)

        if parent1 != parent2:
            if self.rank[parent1] == self.rank[parent2]:
                self.parent[parent2] = parent1
                self.rank[parent1] += 1
            elif self.rank[parent1] < self.rank[parent2]:
                self.parent[parent1] = parent2
            else:
                self.parent[parent2] = parent1 

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        email_to_name = {}
        
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                uf.union(first_email, email)
                email_to_name[email] = name

        parent_to_emails = defaultdict(set)
        for email in email_to_name:
            parent = uf.find(email)
            parent_to_emails[parent].add(email)

        output = []
        for parent, emails in parent_to_emails.items():
            name = email_to_name[parent]
            output.append([name] + sorted(emails))

        return output

# Example usage:
# solution = Solution()
# print(solution.accountsMerge([["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]))
# Output: [["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"], ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
        
        
# @lc code=end

