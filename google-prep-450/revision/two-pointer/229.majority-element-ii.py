#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        elem1, elem2, count1, count2 = None, None, 0, 0

        for elem in nums:
            if elem == elem1:
                count1 += 1
            elif elem == elem2:
                count2 += 1
            elif count1 == 0:
                elem1 = elem
                count1 = 1
            elif count2 == 0:
                elem2 = elem
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        noOfElement = len(nums)

        count1 = 0
        count2 = 0

        for num in nums:
            if num == elem1:
                count1 += 1
            if num == elem2:
                count2 += 1

        result = []

        if count1 > noOfElement//3:
            result.append(elem1)
        if count2 > noOfElement//3:
            result.append(elem2)

        return result


ß
        
# @lc code=end

