class Solution:
    def letterCombinationsHelper(self, currIdx, currArr):
        if currIdx == self.digitsLen:
            self.output.append(''.join(currArr))
            return

        for ch in self.phoneDict[self.digits[currIdx]]:
            currArr.append(ch)
            self.letterCombinationsHelper(currIdx+1, currArr)
            currArr.pop()

        return

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        self.phoneDict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        self.digits = digits 
        self.output = []
        self.digitsLen = len(digits)
        

        self.letterCombinationsHelper(0, [])
        return self.output

        
## slightly optimised version


class Solution:
    def letterCombinationsHelper(self, digits, idx, path, phoneDict, output):
        if idx == len(digits):
            output.append(path)
            return

        for ch in phoneDict[digits[idx]]:
            self.letterCombinationsHelper(digits, idx+1, path+ch, phoneDict, output)

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phoneDict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        output = []
        self.letterCombinationsHelper(digits, 0, "", phoneDict, output)
        return output



