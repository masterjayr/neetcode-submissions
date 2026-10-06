class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # naive approach

        # shortestWindow = float("inf")

        # for L in range(len(nums)):
        #     currSum = nums[L]
        #     for R in range(L+1, len(nums)):
        #         windowSize = R - L + 1

        #         currSum += nums[R]

        #         if currSum >= target:
        #             shortestWindow = min(shortestWindow, windowSize)
        #             break

        # return shortestWindow if shortestWindow != float("inf") else 0

        shortestWindow = float("inf")
        L = 0
        currSum = 0
        for R in range(len(nums)):
            currSum += nums[R]

            while currSum >= target:
                windowSize = R - L + 1
                shortestWindow = min(shortestWindow, windowSize)
                currSum -= nums[L]
                L += 1

        return shortestWindow if shortestWindow != float("inf") else 0
            
            