class Solution:
    def checkIfPalindrom(self,currStr):
        if len(currStr) == 0:
            return False 
        
        start = 0
        end = len(currStr) - 1
        while start < end :
            if currStr[start] != currStr[end]:
                return False 
            
            start += 1
            end -= 1
            
        
        return True


    def partitionHelper(self, currIdx, currArr, s, palindromeStart):
        if currIdx == len(s):
            if palindromeStart == len(s):
                self.output.append(currArr[:])
            return

        if self.checkIfPalindrom(s[palindromeStart:currIdx+1]): 
            currArr.append(s[palindromeStart:currIdx+1])
            self.partitionHelper(currIdx+1, currArr, s, currIdx+1)
            currArr.pop()

        self.partitionHelper(currIdx+1, currArr, s, palindromeStart)
        return

        

    def partition(self, s: str) -> List[List[str]]:
        self.output = []

        self.partitionHelper(0, [], s, 0)
        return self.output
    

## optimised with dp

from typing import List

class Solution:
    def __init__(self):
        self.output = []
        self.memo = {}

    def checkIfPalindrome(self, s, start, end):
        if (start, end) in self.memo:
            return self.memo[(start, end)]
        
        while start < end:
            if s[start] != s[end]:
                self.memo[(start, end)] = False
                return False
            start += 1
            end -= 1
        
        self.memo[(start, end)] = True
        return True

    def partitionHelper(self, s, start, currArr):
        if start == len(s):
            self.output.append(currArr[:])
            return

        for end in range(start, len(s)):
            if self.checkIfPalindrome(s, start, end):
                currArr.append(s[start:end+1])
                self.partitionHelper(s, end+1, currArr)
                currArr.pop()

    def partition(self, s: str) -> List[List[str]]:
        self.output = []
        self.memo = {}
        self.partitionHelper(s, 0, [])
        return self.output