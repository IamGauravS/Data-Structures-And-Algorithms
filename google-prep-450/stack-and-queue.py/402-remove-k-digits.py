class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        numsRemoved = 0

        for ch in num:
            intCh = int(ch)
            
            while stack and numsRemoved < k and stack[-1] > intCh:
                stack.pop()
                numsRemoved += 1

            stack.append(intCh)


        
        while stack and numsRemoved < k:
            stack.pop()
            numsRemoved += 1

        while stack and stack[0] == 0:
            stack.pop(0)

        if not stack:
            return "0"
        
        else:
            ans = ""
            stack = stack[::-1]
            for num in stack: 
                ans += str(num)

            return ans         
