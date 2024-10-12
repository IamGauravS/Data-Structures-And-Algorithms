class Solution:
    
    def longestCommonPrefix(self, strs: List[str]) -> str:

        ## vertical scanning

        if len(strs) == 0 or strs == None:
            return ""
        
        for i in range(len(strs[0])):
            curr = strs[0][i]

            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != curr:
                    return strs[0][:i]
                

        return strs[0]


        