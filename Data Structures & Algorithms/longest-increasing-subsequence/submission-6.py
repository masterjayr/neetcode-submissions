class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # state => i
        # base case -> i == len(nums): return 
        # choices -> every number from i + 1 where i + 1 > i
        # combine -> max between choices so max(LIS, 1 + dfs(j))
        
        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            if i == len(nums):
                return 0

            LIS = 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    LIS = max(LIS, 1 + dfs(j))
            
            cache[i] = LIS
            return cache[i]
        
        # for i in range(len(nums)):
        #     dfs(i)
        # return max(cache.values())

        # converting using dp recipe
        dp = [1] * (len(nums) + 1)
        dp[len(nums)] = 0 # base case

        for i in range(len(nums) -1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)


