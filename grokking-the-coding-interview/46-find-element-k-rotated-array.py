def search(arr, t):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == t:
            return True

        if arr[left] < arr[mid]:  # Left half is sorted
            if arr[left] <= t < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        elif arr[left] > arr[mid]:  # Right half is sorted
            if arr[mid] < t <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:  # arr[left] == arr[mid], can't determine if left half is sorted
            left += 1

    return False




###The worst-case time complexity is O(n) when all elements are the same, but it's still O(log n) for arrays without duplicates