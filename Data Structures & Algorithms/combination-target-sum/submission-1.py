class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combSet = []

        def helper(i, nums, numSet, total):

            if total == target:
                combSet.append(numSet.copy())
                return 

            if i == len(nums) or total > target:
                return

            numSet.append(nums[i])
            helper(i, nums, numSet, total + nums[i])
            numSet.pop()

            helper(i+1, nums, numSet, total)

        helper(0, nums, [], 0)

        return combSet

        