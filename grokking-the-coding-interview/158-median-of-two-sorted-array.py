import sys
def find_median(nums1, nums2):

    # Replace this placeholder return statement with your code

    n1 = len(nums1)
    n2 = len(nums2)
    if n2 < n1:
        nums1, nums2 = nums2, nums1
        
    low = 0
    high = n1 

    left = (n1+n2+1) //2  ## this is the total number which should be on one side of the array

    while (low <= high):
        mid1 = (low+high) // 2
        mid2 = left - mid1   ## amount we will be taking from second array
        
        l1 = -sys.maxsize  ## last element from nums1 in left side
        l2 = -sys.maxsize  ## last element from nums2 in left side
        
        r1 = sys.maxsize  ## first element from nums1 in right side
        r2 = sys.maxsize  ## first element from nums2 in right side
        
        ## mid1 will point to r1 mid 2 will point to r2 
        if mid1 < n1:
            r1 = nums1[mid1]
        if mid2 < n2:
            r2 = nums2[mid2]
        if mid1-1 >= 0:
            l1 = nums1[mid1-1]
        if mid2-1 >= 0:
            l2 = nums2[mid2-1]
            
        if l1 <= r2 and l2 <= r1:
            if (n1+n2) % 2 == 1:
                return max(l1, l2)
            else:
                return (max(l1, l2) + min(r1, r2)) /2 
            
        elif l1 > r2:
            high = mid1-1
        else:
            low = mid1+1
        
        
                
            
        
        
          
        
            
       
