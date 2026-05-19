class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def helper(i, curSet):

            if i == len(nums):
                res.append(curSet.copy())
                return

            curSet.append(nums[i])
            helper(i + 1, curSet)

            curSet.pop()

            while (i + 1) < len(nums) and nums[i] == nums[i+1]:
                i += 1

            helper(i+1, curSet)

        helper(0, [])

        return res
