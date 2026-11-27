class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = {}
        for h in hand:
            count[h] = 1 + count.get(h, 0)

        minH = list(count.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]

            for i in range(first, first+groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if minH[0] != i:
                        return False
                    heapq.heappop(minH)

        return True