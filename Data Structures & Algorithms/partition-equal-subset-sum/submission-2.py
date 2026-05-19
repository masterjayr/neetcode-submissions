class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # brute force attempt
        total = sum(nums)
        if total % 2:
            return False

        targetSum = total // 2
        n = len(nums)
        memo = [[-1] * (targetSum + 1) for _ in range(n+1)]

        def dfsHelper(i, target):
            if target == 0:
                return True
            if i >= n or target < 0:
                return False
            if memo[i][target] != -1:
                return memo[i][target]
            

            memo[i][target] = (dfsHelper(i + 1, target - nums[i]) or dfsHelper(i + 1, target))

            return memo[i][target]

        return dfsHelper(0, targetSum)

