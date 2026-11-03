class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, currList, total):
            if total == 0:
                res.append(currList.copy())
                return 
            if i == len(nums) or total < 0:
                return 

            diff = total - nums[i]
            currList.append(nums[i])
            backtrack(i, currList, diff)

            currList.pop()

            backtrack(i+1, currList, total)

        backtrack(0, [], target)

        return res