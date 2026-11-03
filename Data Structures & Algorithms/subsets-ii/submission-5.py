class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def helper(i, currList):
            if i == len(nums):
                res.append(currList.copy())
                return 

            currList.append(nums[i])
            helper(i+1, currList)

            currList.pop()

            while (i+1) < len(nums) and nums[i] == nums[i+1]:
                i += 1
            
            helper(i+1, currList)
        helper(0, [])
        return res