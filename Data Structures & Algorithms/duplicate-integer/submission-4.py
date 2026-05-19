class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        valSet = set()

        for n in nums:
            if n in valSet:
                return True
            valSet.add(n)

        return False