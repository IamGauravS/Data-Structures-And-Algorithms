def four_sum(arr, target):
    arr.sort()
    result = []
    n = len(arr)
    for i in range(n - 3):
        if i > 0 and arr[i] == arr[i - 1]:
            continue  # Skip duplicates
        for j in range(i + 1, n - 2):
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue  # Skip duplicates
            left = j + 1
            right = n - 1
            while left < right:
                total = arr[i] + arr[j] + arr[left] + arr[right]
                if total == target:
                    result.append([arr[i], arr[j], arr[left], arr[right]])
                    left += 1
                    right -= 1
                    while left < right and arr[left] == arr[left - 1]:
                        left += 1  # Skip duplicates
                    while left < right and arr[right] == arr[right + 1]:
                        right -= 1  # Skip duplicates
                elif total < target:
                    left += 1
                else:
                    right -= 1
    return result
