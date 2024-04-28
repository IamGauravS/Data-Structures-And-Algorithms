class Solution:
    def findRotateSteps(self, ring, key):
        
        rLen, kLen, d = len(ring), len(key), defaultdict(list)
        dist = lambda x,y : min((x-y)%rLen, (y-x)%rLen)

        for i, ch in enumerate(ring): d[ch].append(i)

        @lru_cache(None)
        def dfs(curr = 0,next = 0):

            if next >= kLen: return 0

            return min(dist(curr,k)+dfs(k,next+1) for k in d[key[next]])

        return dfs() + kLen
    



class Solution:
    def findRotateSteps(self, ring, key):
        cache = {}

        def helper(r, k): ## index of ring and index of k
            if k == len(key):
                return 0
            
            if (r,k) in cache:
                return cache[(r,k)]
            
            res = float('inf')

            for i, c in enumerate(ring):
                if c == key[k]:
                    ## distance between character we are targetting and where we are at
                    min_dist = min(
                        abs(r-i), ## between
                        len(ring) - abs(r-i) ## around
                    )
                    min_dist = min_dist + 1 + helper(i, k+1) ## we are at index i

                    res = min(min_dist, res)
            cache[(r,k)] = res
            return res 
        
        return helper(0,0)
    

## bottom up

class Solution:
    def findRotateSteps(self, ring, key):
        dp = [0] * len(ring)

        for k in reversed(range(len(key))):
            next_dp =   [float('inf')]*len(ring)

            for r in range(len(ring)):
                for i, c in enumerate(ring):
                    if c == key[k]:
                        ## distance between character we are targetting and where we are at
                        min_dist = min(
                            abs(r-i), ## between
                            len(ring) - abs(r-i) ## around
                        )
                        min_dist = min_dist + 1 + dp[i] ## we are at index i

                        next_dp[r] = min(min_dist, next_dp[r])

            dp = next_dp.copy()


        return dp[0]