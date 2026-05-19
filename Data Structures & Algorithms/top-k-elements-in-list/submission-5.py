import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            bucket[count].append(num)

        res = []
        for i in range(len(bucket) - 1, 0 , -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res

        return res
        