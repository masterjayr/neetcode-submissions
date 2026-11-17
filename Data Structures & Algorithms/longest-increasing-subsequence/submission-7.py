class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # state => i
        # choices -> dfs(i+1)
        # recurrence -> dfs(i) = 1 + dfs(i+1) if valid

        cache = {}
        def dfs(i):
            if i == len(nums):
                return 0

            if i in cache:
                return cache[i]

            LIS = 1
            #choices
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS = max(LIS, 1 + dfs(j))

            cache[i] = LIS

            return LIS

        for i in range(len(nums)):
            dfs(i)

        return max(list(cache.values()))
            