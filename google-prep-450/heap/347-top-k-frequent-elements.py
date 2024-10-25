import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqNums = {}

        for num in nums:
            if num not in freqNums:
                freqNums[num] = 0
            freqNums[num] += 1

        heap = []
        output = []

        for num, freq in freqNums.items():
            heapq.heappush(heap, (-freq, num))

        while heap and len(output) <k:
            output.append(heapq.heappop(heap)[1])


        return output
