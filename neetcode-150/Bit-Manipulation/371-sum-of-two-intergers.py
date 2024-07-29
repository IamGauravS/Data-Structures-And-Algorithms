class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        axorb = a^b 
        aandb = (a&b) <<1

        return axorb + aandb