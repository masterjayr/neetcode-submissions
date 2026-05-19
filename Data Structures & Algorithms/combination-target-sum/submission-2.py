class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combSet = []

        def backtrack(i, curSet, total):

            if total == target:
                combSet.append(curSet.copy())
                return 

            if i == len(nums) or total > target:
                return

            curSet.append(nums[i])
            backtrack(i, curSet, total + nums[i])
            curSet.pop()

            backtrack(i+1, curSet, total)

        backtrack(0, [], 0)

        return combSet

        