class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        comb = []

        def dfs(i, total, currComb):
            if total == target:
                comb.append(currComb.copy())
                return

            if total > target or i == len(nums):
                return

            currComb.append(nums[i])
            dfs(i, total + nums[i], currComb)
            currComb.pop()
            dfs(i+1, total, currComb)

        dfs(0, 0, [])

        return comb