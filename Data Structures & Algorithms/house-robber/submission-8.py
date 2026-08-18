class Solution:
    def rob(self, nums: List[int]) -> int:
       
       # state = i 
       # choices = i + 1, i + 2
       # combination = max(i + dfs(i+2), dfs(i+1))
       # base case => i == len(nums)
        # cache = {}
        # def dfs(i):
        #     if i >= len(nums):
        #         return 0

        #     if i in cache:
        #         return cache[i]

        #     cache[i] = max(nums[i] + dfs(i + 2), dfs(i+1)) # choices

        #     return cache[i]

        # return dfs(0)

        # converting using recipe
        # initialize dp array with state dimensions and base case as init value
        n = len(nums)
        dp = [0] * (n + 1)
        dp[n-1] = nums[n-1]
        # start loop backwards because recurrence depends on further values i depends on i+1 nd i+2
        for i in range(n - 2, -1, -1):
            dp[i] = max(nums[i] + dp[i + 2], dp[i+1])

        return dp[0]