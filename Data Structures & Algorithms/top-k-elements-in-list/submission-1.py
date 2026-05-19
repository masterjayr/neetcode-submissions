import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        # freq = {1: 1, 2: 2, 3: 3}
        maxHeap = []
        res = []

        for key,val in freq.items():
            heapq.heappush(maxHeap, (-val, key))

        for i in range(k):
            val = heapq.heappop(maxHeap)
            res.append(val[1])

        return res
        