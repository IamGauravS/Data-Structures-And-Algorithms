class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        sorted_strs_with_index = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in sorted_strs_with_index:
                sorted_strs_with_index[sorted_word] = []
                
            sorted_strs_with_index[sorted_word].append(word)
            
        ## add all the values in output
        return sorted_strs_with_index.values()
            
        