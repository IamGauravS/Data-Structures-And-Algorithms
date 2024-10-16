class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        ptr1 = 0 # ptr1 represents pointer to s1 character (start at first char)
        ptr2 = 0 # ptr2 represents pointer to s2 character (start at first char)
        cur_max = float('inf')
        res = ''
        start = 0 # start represents the start of the valid subsequence
        end = 0 # start represents the start of the valid subsequence
        while ptr1 < len(s1):
            # something only happens if the next char in ptr2 is hit
            if s1[ptr1] == s2[ptr2]:
                ptr2+=1 

                # only care about checking for valid subsequence
                # if all the chars in s2 are hit (meaning ptr2 == len(s2))
                if ptr2 == len(s2):
                    # at this point we know we have the valid subsequence
                    # BUT, it's not necessarily the minimum

                    # this is to minimize the valid subsequence
                    end = ptr1
                    ptr2 -= 1

                    # point ptr2 back to last character of s2
                    # iterate backwards on s1 characters until all the characters of s2 are seen
                    # this is guaranteed to yield a result
                    while ptr2 >= 0:
                        if s1[ptr1] == s2[ptr2]:
                            ptr2-=1
                        ptr1 -= 1
                    
                    # since ptr1 will overshoot we need to offset by 1
                    ptr1 += 1

                    # at this point the start of the MINIMUM subsequence must be at ptr1
                    start = ptr1 

                    # standard check to only replace the the last answer if it's less than the current 
                    # minimum subsequence
                    if end-start < cur_max:
                        cur_max = end-start
                        res = s1[start:end+1]              
                    
                    # probably unecessary but semantically you want to start 
                    # finding valid subsequence again from scratch here
                    ptr2 = 0 
            ptr1+=1
        return res 