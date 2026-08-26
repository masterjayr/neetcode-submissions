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
        cache = {}
        def dfs(i, total):
            if (i, total) in cache:
                return cache[(i, total)]
            if total == 0:
                return True
            if i == len(nums) or total < 0:
                return False

            res = dfs(i + 1, total - nums[i]) or dfs(i+1, total)

            cache[(i, total)] = res

            return cache[(i, total)]

        return dfs(0, target)