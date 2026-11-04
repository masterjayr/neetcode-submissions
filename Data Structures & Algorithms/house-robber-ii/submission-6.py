class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.rob1(nums[1:]), self.rob1(nums[:-1]))

    def rob1(self, nums):
        rob1, rob2 = 0, 0

        for i in range(len(nums)-1, -1, -1):
            temp = rob1
            rob1 = max(nums[i] + rob2, rob1)
            rob2 = temp
        
        return rob1