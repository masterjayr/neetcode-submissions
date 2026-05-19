class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()

        for n in nums:
            unique.add(n)

        return False if len(nums) == len(unique) else True