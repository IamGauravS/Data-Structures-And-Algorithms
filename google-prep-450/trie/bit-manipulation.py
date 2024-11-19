class Solution:
    def XOR(self, n, m):
        # Code here: Compute the XOR of n and m
        return n ^ m

    def check(self, a, b):
        # Code here: Check if the b-th bit in a is set (1)
        return (a & (1 << b)) != 0

    def setBit(self, c, d):
        # Code here: Set the d-th bit in c
        return c | (1 << d)
