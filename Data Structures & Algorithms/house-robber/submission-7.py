class Solution:
    def rob(self, nums: List[int]) -> int:
       
       # state = i 
       # choices = i + 1, i + 2
       # combination = max(i + dfs(i+2), dfs(i+1))
       # base case => i == len(nums)
        cache = {}
        def dfs(i):
            if i >= len(nums):
                return 0

            if i in cache:
                return cache[i]

            cache[i] = max(nums[i] + dfs(i + 2), dfs(i+1))

            return cache[i]

        return dfs(0)