class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # using dp recipe
        # state -> i, target so 2D DP
        # base case -> total == target return True, if i == len(nums) and total != target: return FAlse
        # choices -> include i or don't include i so dfs(i+1, total + nums[i]) or dfs(i+1, total)
        # combine -> OR if either is True then return True
        totalSum = sum(nums)
        if totalSum % 2: return False

        target = totalSum // 2
        cache = [[-1] * (target + 1) for i in range(len(nums))]
        def dfs(i, total):
            if total == 0:
                return True
            if i == len(nums) or total < 0:
                return False
            if cache[i][total] != -1:
                return cache[i][total]

            include = dfs(i+1, total - nums[i])
            skip = dfs(i+1, total)
            res = include or skip

            cache[i][total] = res

            return cache[i][total]

        # return dfs(0, target)
        n = len(nums)
        dp = [[False] * (target + 1) for i in range(n+1)]
        dp[n][0] = True # base case

        # loop backwards
        for i in range(n - 1, -1, -1):
            for total in range(target+1):
                dp[i][total] = dp[i+1][total] # skip

                if total - nums[i] >= 0: #include
                    dp[i][total] = dp[i][total] or dp[i+1][total - nums[i]]

        return dp[0][target]
                

