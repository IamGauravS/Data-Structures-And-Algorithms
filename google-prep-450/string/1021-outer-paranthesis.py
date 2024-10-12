class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        count = 0


        for ch in s:
            if ch == '(':
                count += 1
                if count > 1:
                    res.append(ch)

            else:
                count -= 1
                if count > 0:
                    res.append(ch)


        return ''.join(res)