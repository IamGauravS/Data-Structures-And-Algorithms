def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_select(arr, k, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pi = partition(arr, low, high)
        if k < pi:
            return quick_select(arr, k, low, pi - 1)
        elif k > pi:
            return quick_select(arr, k, pi + 1, high)
        else:
            return arr[pi]

    return arr[low]