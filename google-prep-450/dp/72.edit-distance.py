#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistanceHelper(self, word1, word2, index1, index2):
        """
        This is the helper function that gets the minimum edit distance between
        two words. It tries all the paths available to us (replace, insert and delete)
        and chooses the one with the least value. 

        Args:
            word1 (str) : input word 1
            word2 (str) : input word 2
            index1 (int) : current index of word1
            index2 (int) : current index of word2

        Returns:
            editDistance : minimum edit distance to convert word1 to word2 for current index1 and index2

        """
        ## if both words are already equal
        if word1 == word2:
            return 0
        
        elif index1 == len(word1):
            ## all insert operations
            self.dp[(index1, index2)] =  len(word2) - index2 
            
            
        elif index2 == len(word2):
            ## all delete operations
            self.dp[(index1, index2)] = len(word1) - index1 
            
        ## if we have already processed
        elif (index1, index2) in self.dp:
            return self.dp[(index1, index2)]
        
        ## if both the characters are equal then we greedily take it and move to next index
        elif word1[index1] == word2[index2]:
            noOfWays = self.minDistanceHelper(word1, word2, index1+1, index2+1)
            self.dp[(index1, index2)] = noOfWays

        else:
            noOfWays = float('inf')
            ##  insert operation

            noOfWays = min(noOfWays, 1 + self.minDistanceHelper(word1, word2, index1, index2+1))

            ## delete operation
            noOfWays = min(noOfWays, 1 + self.minDistanceHelper(word1, word2, index1+1, index2))

            ## replace operation
            noOfWays = min(noOfWays, 1 + self.minDistanceHelper(word1, word2, index1+1, index2+1))

            self.dp[(index1, index2)] = noOfWays
            
        return self.dp[(index1, index2)]


    def minDistance(self, word1: str, word2: str) -> int:
        """
        This function uses memoization to calculate the minimum operations required
        to convert word1 to word2. 

        Args:
            word1 ; word which we want to convert to word2
            word2 : target word
        Returns:
            minimumEditDistance : no of operations required to convert word1 to word2

        """

        if word1 == word2:
            return 0
        
        self.dp = {}
        
        self.minDistanceHelper(word1, word2, 0, 0)

        return self.dp[(0, 0)]
        

        
# @lc code=end

