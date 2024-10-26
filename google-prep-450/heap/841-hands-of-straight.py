import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        freqCount = {}
        for card in hand:
            if card not in freqCount:
                freqCount[card] = 0
            freqCount[card] += 1


        heap = []
        for card, freq in freqCount.items():
            heapq.heappush(heap, (card, freq))

        while heap:
            prevCard , minfreq = None, None
            noOfCards = groupSize
            store = []

            while heap and noOfCards > 0:
                currCard, currFreq = heapq.heappop(heap)
                

                if prevCard == None:
                    prevCard, minfreq = currCard, currFreq

                else:
                    if currCard - prevCard != 1 or currFreq - minfreq < 0:
                        return False 

                    currFreq = currFreq - minfreq

                    if currFreq > 0:
                        store.append((currCard, currFreq))

                noOfCards -= 1

            if noOfCards != 0:
                return False 

            for item in store:
                heapq.heappush(heap, item)

        return True


            


            