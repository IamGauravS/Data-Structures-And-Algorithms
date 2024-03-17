def get_permutation(nums, k):
    fact = [1]
    numbers = nums[:]
    
    # Calculate factorial for each number
    for i in range(1, len(nums)):
        fact.append(fact[-1] * i)
    
    # Adjust k to be 0-based index
    k -= 1
    ans = []
    
    for i in range(len(nums), 0, -1):
        id = k // fact[i-1]
        k %= fact[i-1]
        ans.append(numbers[id])
        numbers.pop(id)
    
    return ans