class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def backtrack(i, currSum):
            if i == len(nums):
                return 1 if target  == currSum else 0

            dp[(i, currSum)] =  (backtrack(i+1, currSum + nums[i]) +
                                    backtrack(i+1, currSum - nums[i]))

            return  dp[(i, currSum)]

        return backtrack(0, 0)