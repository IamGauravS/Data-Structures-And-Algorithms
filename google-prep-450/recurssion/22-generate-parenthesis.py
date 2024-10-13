from typing import List

class Solution:
    def generateParenthesisHelper(self, noOfOpenBrackets, noOfClosedBrackets, n, currStr):
        if noOfOpenBrackets == n and noOfClosedBrackets == n:
            self.wellFormedParentheses.append(currStr)
            return

        if noOfOpenBrackets < n:
            self.generateParenthesisHelper(noOfOpenBrackets + 1, noOfClosedBrackets, n, currStr + '(')

        if noOfClosedBrackets < noOfOpenBrackets:
            self.generateParenthesisHelper(noOfOpenBrackets, noOfClosedBrackets + 1, n, currStr + ')')

    def generateParenthesis(self, n: int) -> List[str]:
        self.wellFormedParentheses = []
        self.generateParenthesisHelper(0, 0, n, "")
        return self.wellFormedParentheses
    


## ANOTHER way to do it

class Solution:
    def generateParenthesisHelper(self, noOfOpenBrackets, noOfClosedBrackets, n, currStr):
        # Base case: If the number of open and closed brackets equals `n`, add the current string to result
        if noOfOpenBrackets == n and noOfClosedBrackets == n:
            self.wellFormedParentheses.append(currStr)
            return

        # Add open bracket if it's still possible
        if noOfOpenBrackets < n:
            currStr += '('  # Add open bracket
            self.generateParenthesisHelper(noOfOpenBrackets + 1, noOfClosedBrackets, n, currStr)
            currStr = currStr[:-1]  # Backtrack by removing the last character (open bracket)

        # Add closed bracket if there are unmatched open brackets
        if noOfClosedBrackets < noOfOpenBrackets:
            currStr += ')'  # Add closed bracket
            self.generateParenthesisHelper(noOfOpenBrackets, noOfClosedBrackets + 1, n, currStr)
            currStr = currStr[:-1]  # Backtrack by removing the last character (closed bracket)

    def generateParenthesis(self, n: int):
        self.wellFormedParentheses = []
        self.generateParenthesisHelper(0, 0, n, "")
        return self.wellFormedParentheses
