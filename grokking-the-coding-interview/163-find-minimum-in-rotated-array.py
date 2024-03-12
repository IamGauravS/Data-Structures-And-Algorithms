def find_min_in_rotated_array(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        mid = (start + end) // 2

        # If the middle element is greater than the last element, the minimum value must be in the right half
        if arr[mid] > arr[end]:
            start = mid + 1
        else:
            # Otherwise, the minimum value must be in the left half
            end = mid

    # When start == end, we've found the minimum value
    return arr[start]