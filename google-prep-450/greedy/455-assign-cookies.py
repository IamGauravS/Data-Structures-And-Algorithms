class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g, reverse=True)
        s = sorted(s, reverse=True)

        satisfiedChildren = 0

        i,j = 0, 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                satisfiedChildren += 1
                i += 1
                j += 1
            else:
                i += 1


        return satisfiedChildren
