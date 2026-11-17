class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # state => i
        # choices -> dfs(i+1)
        # recurrence -> dfs(i) = 1 + dfs(i+1) if valid
        
        dp = [1] * (len(nums) + 1)
        dp[-1] = 0

        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        
        return max(dp)
        

        
            