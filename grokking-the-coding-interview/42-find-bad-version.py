import main as api_call

def is_bad_version(v): # is_bad_version() is the API function that returns true or false depending upon whether the provided version ID is bad or not
    return api_call.is_bad(v)
# ----------------------------------------------- 

def first_bad_version(n):
    # Initialize the number of API calls to 0
    number_of_api_calls = 0

    # Initialize two pointers, left and right, to the start and end of the version range
    left = 1
    right = n

    # Perform a binary search
    while left < right:
        # Calculate the middle version
        mid = left + (right - left) // 2

        # Increment the number of API calls
        number_of_api_calls += 1

        # If the middle version is bad, the first bad version must be to its left (including itself)
        if is_bad_version(mid):
            right = mid
        else:
            # If the middle version is not bad, the first bad version must be to its right
            left = mid + 1

    
    

    # Return the first bad version and the number of API calls
    return left, number_of_api_calls


##In a binary search, you don't need to check the previous version every time you find a bad version. Instead, you should continue the binary search until the search space is narrowed down to a single element. This is because the first bad version is the one where is_bad_version(mid) is True and is_bad_version(mid - 1) is False, and the binary search will naturally find this version when the search space is narrowed down to a single element.
