class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * n

        def dfsHelper(i):

            if memo[i] != -1:
                return memo[i]

            LIS = 1

            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    LIS = max(LIS, 1 + dfsHelper(j))
            memo[i] = LIS
            return LIS

        return max(dfsHelper(i) for i in range(len(nums)))

