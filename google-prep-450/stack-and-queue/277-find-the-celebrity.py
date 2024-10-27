# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        self.n = n
        celebrityCandidate = 0

        for i in range(n):
            if knows(celebrityCandidate, i):
                celebrityCandidate = i

        if self.isCelebrity(celebrityCandidate):
            return celebrityCandidate

        return -1

    def isCelebrity(self, i):
        for j in range(self.n):
            if i == j:
                continue
            if knows(i, j) or not knows(j, i):
                return False 

        return True