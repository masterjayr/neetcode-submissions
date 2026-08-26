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
        dp = set()
        dp.add(0)

        for i in range(len(nums)):
            nextDp = set()
            for t in dp:
                if nums[i] + t == target:
                    return True
                nextDp.add(nums[i] + t)
                nextDp.add(t)
            dp = nextDp

        return True if target in dp else False


                

