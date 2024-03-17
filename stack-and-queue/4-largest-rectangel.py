from collections import deque

def sliding_window_maximum(nums, k):
    if not nums:
        return []

    result = []
    window = deque()

    # Process the first k elements separately to initialize the window
    for i in range(k):
        # Remove elements smaller than the current element from the end of the deque
        while window and nums[i] >= nums[window[-1]]:
            window.pop()
        window.append(i)

    # Process the remaining elements
    for i in range(k, len(nums)):
        # Append the maximum element from the window to the result
        result.append(nums[window[0]])

        # Remove elements outside the current window
        while window and window[0] <= i - k:
            window.popleft()

        # Remove elements smaller than the current element from the end of the deque
        while window and nums[i] >= nums[window[-1]]:
            window.pop()
        window.append(i)

    # Append the maximum element from the last window to the result
    result.append(nums[window[0]])

    return result

# Example usage:
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(sliding_window_maximum(nums, k))  # Output: [3, 3, 5, 5, 6, 7]
