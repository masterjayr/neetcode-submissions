class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combSet = []

        def helper(i, nums, curSet, total):

            if total == target:
                combSet.append(curSet.copy())
                return

            if i == len(nums) or total > target:
                return 

            # choice 1
            curSet.append(nums[i])
            helper(i, nums, curSet, total + nums[i])

            # choice 2
            curSet.pop()
            helper(i+1, nums, curSet, total)
        helper(0, nums, [], 0)
        return list(combSet)