class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # brute force attempt with cache
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        cache = {}

        def dfs(i, t):
            if t == 0:
                return True
            if i == len(nums) or t < 0:
                return False 
            if (i, t) in cache:
                return cache[(i, t)]
            
            cache[(i, t)] = dfs(i + 1, t - nums[i]) or dfs(i+1, t)

            return cache[(i, t)]

        # return dfs(0, target)

        # true dp solution
        dp = [[False] * (target + 1) for _ in range(len(nums) + 1)]

        for i in range(len(nums) + 1):
            dp[i][0] = True

        for i in range(len(nums) -  1, -1, -1):
            for t in range(1, target + 1):
                dp[i][t] = dp[i+1][t] or (t >= nums[i] and dp[i+1][t - nums[i]])

        return dp[0][target]
















        # total = sum(nums)
        # if total % 2:
        #     return False 

        # target = total // 2
        # dp = set()
        # dp.add(0)

        # for i in range(len(nums)-1, -1, -1):
        #     nextDp = set()
        #     for t in dp:
        #         nextDp.add(t + nums[i])
        #         nextDp.add(t)

        #     dp = nextDp

        # return True if target in nextDp else False
