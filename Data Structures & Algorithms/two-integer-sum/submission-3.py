class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}

        for i, v in enumerate(nums):
            val = target - v

            if val in numToIndex:
                return [numToIndex[val], i]

            numToIndex[v] = i
