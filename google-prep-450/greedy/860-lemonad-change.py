from typing import List

class Solution:
    def __init__(self):
        self.currBills = {5: 0, 10: 0, 20: 0}

    def canMake(self, amount: int) -> bool:
        # Try to use the largest bills first
        if amount >= 10 and self.currBills[10] > 0:
            amount -= 10
            self.currBills[10] -= 1
        while amount >= 5 and self.currBills[5] > 0:
            amount -= 5
            self.currBills[5] -= 1
        return amount == 0

    def lemonadeChange(self, bills: List[int]) -> bool:
        for bill in bills:
            change = bill - 5
            if not self.canMake(change):
                return False
            self.currBills[bill] += 1
        return True

# Example usage
solution = Solution()
bills = [5, 5, 5, 10, 20]
print(solution.lemonadeChange(bills))  # Output: True