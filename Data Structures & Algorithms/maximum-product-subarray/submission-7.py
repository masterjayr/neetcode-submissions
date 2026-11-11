class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        currMax, currMin = 1, 1
        maxProd = 0
        for n in nums:

            temp = currMax * n
            currMax = max(currMax * n, currMin*n, n)
            currMin = min(temp, currMin*n, n)
            maxProd = max(currMax, currMin, maxProd)

        return maxProd
