class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0,1]

        output = [0,1]

        for i in range(2, n+1):
            output.append(i%2 + output[i//2])


        return output


## optimised

class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)

        for i in range(1, n + 1):
            output[i] = i % 2 + output[i // 2]

        return output


## using bitwise operators

class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)

        for i in range(1, n + 1):
            output[i] = (i & 1) + output[i >> 1]  ## last bit plus shift by 1

        return output