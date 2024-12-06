#
# @lc app=leetcode id=904 lang=python3
#
# [904] Fruit Into Baskets
#

# @lc code=start
from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        start = 0
        maxFruits = 0
        fruitSet = defaultdict(int)

        for end in range(len(fruits)):
            curr = fruits[end]
            fruitSet[curr] += 1

            while len(fruitSet) > 2:
                fruitSet[fruits[start]] -= 1
                if fruitSet[fruits[start]] == 0:
                    del fruitSet[fruits[start]]

                start += 1
                
            
            maxFruits = max(maxFruits, end-start+1)


        return maxFruits


        
# @lc code=end

