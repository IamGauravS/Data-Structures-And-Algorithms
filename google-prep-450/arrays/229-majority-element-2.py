class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        elem1, elem2, count1, count2 = None, None, 0, 0

        for num in nums:
            if num == elem1:
                count1 += 1
            
            elif num == elem2:
                count2 += 1

            elif count1 == 0:
                elem1 = num 

            elif count2 == 0:
                elem2 = num 

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
            