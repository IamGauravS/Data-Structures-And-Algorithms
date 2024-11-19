#
# @lc app=leetcode id=1707 lang=python3
#
# [1707] Maximum XOR With an Element From Array
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.data = [None, None]  # For binary digits 0 and 1

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def get_bit_representation(self, num, bit_length=32):
        return bin(num)[2:].zfill(bit_length)

    def insert(self, number):
        currNode = self.root
        bitNum = self.get_bit_representation(number)

        for ch in bitNum:
            ind = int(ch)
            if currNode.data[ind] is None:
                currNode.data[ind] = TrieNode()
            currNode = currNode.data[ind]

    def findMaxXor(self, number):
        currNode = self.root
        bitNum = self.get_bit_representation(number)
        maxXorBits = ""

        for ch in bitNum:
            ind = int(ch)
            oppositeBit = 1 - ind

            if currNode.data[oppositeBit] is not None:
                maxXorBits += "1"
                currNode = currNode.data[oppositeBit]
            elif currNode.data[ind] is not None:
                maxXorBits += "0"
                currNode = currNode.data[ind]
            else:
                return 0  # No valid path exists

        return int(maxXorBits, 2)

class Solution:
    def maximizeXor(self, nums, queries):
        nums.sort()  # Sort nums for efficient insertion into the Trie
        queries_with_indices = [(q[0], q[1], i) for i, q in enumerate(queries)]
        queries_with_indices.sort(key=lambda x: x[1])  # Sort queries by mi

        trie = Trie()
        output = [-1] * len(queries)
        idx = 0

        for xi, mi, originalIndex in queries_with_indices:
            # Insert all nums <= mi into the Trie
            while idx < len(nums) and nums[idx] <= mi:
                trie.insert(nums[idx])
                idx += 1

            # Compute maximum XOR for the current query
            if idx > 0:  # Trie is non-empty
                output[originalIndex] = trie.findMaxXor(xi)

        return output


        
# @lc code=end

