class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        sign = 1 if x >= 0 else -1
        x *= sign

        while x:
            result = result * 10 + x % 10
            x //= 10

        result *= sign
        if result < -2**31 or result > 2**31 - 1:
            return 0

        return result