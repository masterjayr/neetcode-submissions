class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # brute force attempt
        total = sum(nums)
        if total % 2:
            return False 

        target = total // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums)-1, -1, -1):
            nextDp = set()
            for t in dp:
                nextDp.add(t + nums[i])
                nextDp.add(t)

            dp = nextDp

        return True if target in nextDp else False
