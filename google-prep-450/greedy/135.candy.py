#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        totalCandy = 1
        i = 1 

        while (i < len(ratings)):
            if ratings[i] == ratings[i-1]:
                totalCandy += 1
                i += 1
                continue 

            peak = 1
            while i < len(ratings) and ratings[i] > ratings[i -1]:
                peak += 1
                i += 1
                totalCandy += peak 

            down = 1
            while i < len(ratings) and ratings[i] < ratings[i-1]:
                
                i += 1
                totalCandy += down 
                down += 1

            if down > peak:
                totalCandy += (down - peak)

        return totalCandy 


# @lc code=end

