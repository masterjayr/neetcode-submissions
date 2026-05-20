class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, curSet):
            if i == len(nums):
                res.append(curSet.copy())
                return

            curSet.append(nums[i])
            dfs(i+1, curSet)
            curSet.pop()

            while i + 1 < len(nums) and nums[i+1] == nums[i]:
                i += 1

            dfs(i+1, curSet)
        dfs(0, [])
        return res