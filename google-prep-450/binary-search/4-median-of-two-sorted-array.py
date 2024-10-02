class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        

        m, n = len(nums1), len(nums2)

        low, high = 0, m

        

        while low <= high:
            mid1 = (low + high)//2
            mid2 = (m + n + 1) // 2 - mid1

            l1 = float('-inf') if mid1 == 0 else nums1[mid1 - 1]
            r1 = float('inf') if mid1 == m else nums1[mid1]
            l2 = float('-inf') if mid2 == 0 else nums2[mid2 - 1]
            r2 = float('inf') if mid2 == n else nums2[mid2]

            if l1 <= r2 and l2 <= r1:
                if (m + n) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return max(l1, l2)
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1


        
## for kth element

class Solution:
    def findKthElement(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m

        while low <= high:
            mid1 = (low + high) // 2
            mid2 = k - mid1

            l1 = float('-inf') if mid1 == 0 else nums1[mid1 - 1]
            r1 = float('inf') if mid1 == m else nums1[mid1]
            l2 = float('-inf') if mid2 == 0 else nums2[mid2 - 1]
            r2 = float('inf') if mid2 == n else nums2[mid2]

            if l1 <= r2 and l2 <= r1:
                return max(l1, l2)
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1

        return -1  # Should never reach here for valid input



