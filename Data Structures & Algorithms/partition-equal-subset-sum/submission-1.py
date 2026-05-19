class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # brute force attempt
        if sum(nums) % 2:
            return False

        targetSum = sum(nums) / 2


        
        def dfsHelper(i, target):

            if i >= len(nums):
                return target == 0

            if target < 0:
                return False

            include = dfsHelper(i + 1, target - nums[i])

            skip = dfsHelper(i + 1, target)

            return include or skip

        return dfsHelper(0, targetSum)

