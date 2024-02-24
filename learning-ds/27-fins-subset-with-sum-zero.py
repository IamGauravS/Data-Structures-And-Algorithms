def find_sub_zero(my_list):
    # Create a set to store the prefix sums
    sum_set = set()

    # Initialize sum of elements
    sum = 0

    # Traverse through the given list
    for i in range(len(my_list)):
        
        # Add current element to sum
        sum += my_list[i]

        # If sum is 0, or sum already exists in set, we found a subarray with zero sum
        # The reason is that we are calculating the "prefix sum" up to the current element.
        # If at any point, the prefix sum becomes zero, or if the prefix sum has been seen before,
        # it means that the sum of the elements between the previous occurrence and the current element is zero.
        if sum == 0 or sum in sum_set:
            return True

        # Add sum to set
        sum_set.add(sum)
    
    # If we reach here, then no subarray has zero sum
    return False