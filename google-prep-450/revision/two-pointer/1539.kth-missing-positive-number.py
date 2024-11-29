#
# @lc app=leetcode id=1539 lang=python3
#
# [1539] Kth Missing Positive Number
#

# @lc code=start
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        start = 0
        end = len(arr) - 1

        while start <= end:
            mid = (start+end)//2

            noOfmissingnumbers = arr[mid] - (mid+1)

            if noOfmissingnumbers < k:
                start = mid + 1
            else:
                end = mid - 1

        if end < 0:
            # If all missing numbers are before the first element
            return k
        else:
            # Calculate the kth missing number
            noOfMissingNumbers = arr[end] - (end + 1)
            return arr[end] + (k - noOfMissingNumbers)
        
# @lc code=end
