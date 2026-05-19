class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        return max(self.dfsHelper(i, nums) for i in range(len(nums)))

    def dfsHelper(self, i, nums):

        if i >= len(nums):
            return 0

        res = 1

        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                res = max(res, 1 + self.dfsHelper(j, nums))

        return res

