class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # will come back to this

        dp = {}

        def backtrack(i, curr_sum):
            if i == len(nums):
                return 1 if curr_sum == target else 0

            if (i, curr_sum) in dp:
                return dp[(i, curr_sum)]

            dp[(i, curr_sum)] = backtrack(i+1, curr_sum + nums[i]) + backtrack(i+1, curr_sum-nums[i])

            return dp[(i, curr_sum)]

        return backtrack(0, 0)