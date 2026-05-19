class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = set()

        for n in nums:
            if n in freq:
                return True
            freq.add(n)
        
        return False