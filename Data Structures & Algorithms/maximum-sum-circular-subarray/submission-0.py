class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMax, currMin = 0, 0
        globalMax, globalMin = nums[0], nums[0]
        total = 0

        for n in nums:
            total += n
            currMax = max(currMax, 0) + n
            currMin = min(currMin, 0) + n


            globalMax = max(currMax, globalMax)
            globalMin = min(currMin, globalMin)


        return max(globalMax, total-globalMin) if globalMax > 0 else globalMax
