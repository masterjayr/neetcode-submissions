class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
    
    # house robber 1
    def helper(self, nums):
        one, two = 0, 0

        for i in range(len(nums) - 1, -1, -1):
            tmp = one
            one = max(nums[i] + two, one)
            two = tmp

        return one