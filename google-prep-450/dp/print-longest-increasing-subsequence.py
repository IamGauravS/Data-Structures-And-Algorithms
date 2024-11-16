from collections import defaultdict
class Solution:
    def longestIncreasingSubsequence(self, N, arr):
        # Code here
        dp = [1]*len(arr)
        lisStore = defaultdict(list)
        
        for i in range(len(arr)):
            maxJ = -1
            for j in range(i):
                if arr[j] < arr[i] and dp[j] +1 > dp[i]:
                    maxJ = j
                    dp[i] = dp[j] + 1
            if maxJ == -1:
                lisStore[i] = [arr[i]]
            else:
                lisStore[i] = lisStore[maxJ][:] + [arr[i]]
                
                
        max_index = dp.index(max(dp))
        return lisStore[max_index]
    


from bisect import bisect_left

class Solution:
    def longestIncreasingSubsequence(self, N, arr):
        if N == 0:
            return []

        # Array to store the smallest tail value for all increasing subsequences of different lengths
        tails = []
        # Array to store the actual LIS
        lis = []

        for num in arr:
            pos = bisect_left(tails, num)
            if pos < len(tails):
                tails[pos] = num
            else:
                tails.append(num)

            if pos == len(lis):
                lis.append(num)
            else:
                lis[pos] = num

        return lis

# Example usage:
solution = Solution()
print(solution.longestIncreasingSubsequence(6, [5, 8, 3, 7, 9, 1]))  # Output: [5, 7, 9]