#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def recursion(self, x, times, n):
        if times == n:
            return x 

        currChar = x[0]
        count = 1
        answer = ""

        for i in range(1, len(x)):
            if x[i] == currChar:
                count += 1
            else:
                answer += str(count) + currChar
                count = 1
                currChar = x[i]

        answer += str(count) + currChar
        return self.recursion(answer, times+1, n)


    def countAndSay(self, n: int) -> str:
        return self.recursion("1", 1, n)

        
# @lc code=end

