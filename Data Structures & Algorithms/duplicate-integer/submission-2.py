class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}

        for n in nums:
            freq[n]  = freq.get(n, 0) + 1

        for key, value in freq.items():
            if value > 1:
                return True

        return False