#
# @lc app=leetcode id=421 lang=python3
#
# [421] Maximum XOR of Two Numbers in an Array
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.data = [None]*2

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def get_bit_representation(self, num: int, bit_length: int = 32) -> str:
        return bin(num)[2:].zfill(bit_length)

    def insert(self, number):
        currNode = self.root
        bitNum  = self.get_bit_representation(number)

        for ch in bitNum:
            ind = int(ch)
            if currNode.data[ind] == None:
                currNode.data[ind] = TrieNode()
            currNode = currNode.data[ind]

        return 
    
    def bits_to_number(self, bit_string: str) -> int:
        return int(bit_string, 2)
    
    def findMaxXor(self, number):
        currNode = self.root 
        bitNum = self.get_bit_representation(number)
        outputNuminBits = ""

        for ch in bitNum:
            ind = int(ch)
            if ind == 1:
                if currNode.data[0] != None:
                    currNode = currNode.data[0]
                    outputNuminBits += '0'
                else:
                    currNode = currNode.data[1]
                    outputNuminBits += '1'
            else:
                if currNode.data[1] != None:
                    currNode = currNode.data[1]
                    outputNuminBits += '1'
                else:
                    currNode = currNode.data[0]
                    outputNuminBits += '0'

        return self.bits_to_number(outputNuminBits)

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        trie = Trie()
        for num in nums:
            trie.insert(num)

        maxXor = 0
        for num in nums:
            maxXor = max(maxXor, num^trie.findMaxXor(num))

        return maxXor
        
# @lc code=end

