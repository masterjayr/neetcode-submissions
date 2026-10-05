class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # using kadanes algorithm - subarray with largest sum
        # brute force will be to check all subarrays
        # eliminating repeated work using kadanes algorithm

        currSum = 0
        maxSum = nums[0]

        for n in nums:
            currSum = max(currSum, 0)

            currSum += n

            maxSum = max(maxSum, currSum)

        return maxSum