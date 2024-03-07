def merge_sorted(nums1, m, nums2, n):
    # Start from the end of nums1 and nums2. Compare elements and put the larger one at the end of nums1.
    # If there are still elements left in nums2 after all elements in nums1 have been processed, copy them to nums1.
    while m > 0 and n > 0:
        if nums1[m-1] > nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]
    return nums1