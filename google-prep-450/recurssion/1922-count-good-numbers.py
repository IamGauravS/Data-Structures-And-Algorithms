class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        noOfOdd = n // 2
        noOfEven = n - noOfOdd

        noOfGoodNumbers = pow(4, noOfOdd, MOD) * pow(5, noOfEven, MOD) 

        return noOfGoodNumbers % MOD
