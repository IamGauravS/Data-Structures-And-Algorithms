class Solution:
    def letterCombinationsHelper(self, digits,  subSet, index):
        if index == len(digits):
            self.output.append("".join(subSet))
            return
            
        for letter in self.numberLetterHashSet[digits[index]]:
            subSet.append(letter)
            self.letterCombinationsHelper(digits,  subSet, index+1)
            subSet.pop()
            
        return 
    
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        self.numberLetterHashSet = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        self.output = []
        subSet = []
        index = 0
        self.letterCombinationsHelper(digits,  subSet, index)
        return self.output

        
        