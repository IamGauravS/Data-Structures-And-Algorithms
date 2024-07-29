class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        ## if sum of gas is greater than sum of cost then only solution is possible
        if sum(gas) - sum(cost) < 0:
            return -1

        diff = [gas[i]-cost[i] for i in range(len(gas))]
        total = 0
        start = 0
        for i in range(len(diff)):
            total += diff[i]

            if total < 0:
                total = 0
                start = i + 1


        return start
