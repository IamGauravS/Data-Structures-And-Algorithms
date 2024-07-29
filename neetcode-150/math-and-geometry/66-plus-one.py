class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if digits[-1] != 9:
            digits[-1] = digits[-1] + 1
            return digits
        
        number = int("".join(map(str, digits)))
        number = number + 1

        return list(map(int, str(number)))
    


## most optimal

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

        return [1] + digits