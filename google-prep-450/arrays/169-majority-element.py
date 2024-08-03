from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Initialize the majority element and its count
        majorityElement = nums[0]
        elementCount = 1

        # Iterate through the list starting from the second element
        for i in range(1, len(nums)):
            if nums[i] == majorityElement:
                # Increment the count if the current element is the same as the majority element
                elementCount += 1
            else:
                # Decrement the count if the current element is different
                elementCount -= 1
                # If the count reaches zero, update the majority element and reset the count
                if elementCount == 0:
                    majorityElement = nums[i]
                    elementCount = 1 

        # Return the majority element
        return majorityElement