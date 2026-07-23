class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}
        def dfs(i):
            if i == len(nums) - 1:
                return 1
            if i in cache:
                return cache[i]
            lis = 1
            # choices from index i
            for j in range(i+1, len(nums)):
                # if valid choice meaning increasing
                if nums[i] < nums[j]:
                    lis = max(lis, 1 + dfs(j))
            
            cache[i] = lis
            return cache[i]

        return max(dfs(i) for i in range(len(nums)))