class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 1 or x == -1:
            return x

        if n < 0:
            n = -1*n
            x = 1/x

        if n%2 == 0:
            half = self.myPow(x, n/2)
            return half*half

        else:
            return x*self.myPow(x, n-1)