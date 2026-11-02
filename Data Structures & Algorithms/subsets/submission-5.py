class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def helper(i, currList):
            if i == len(nums):
                res.append(currList.copy())
                return 


            currList.append(nums[i])
            helper(i+1, currList)
            currList.pop()

            helper(i+1, currList)

        helper(0, [])

        return res