class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        for val in freq.values():
            if val > 1:
                return True

        return False