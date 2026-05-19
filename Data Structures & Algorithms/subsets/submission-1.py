class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        currSet = []
        subSets = []

        def helper(i, nums, currSet, subSets):

            if i == len(nums):
                subSets.append(currSet.copy())
                return 

            
            currSet.append(nums[i])
            helper(i + 1, nums, currSet, subSets)
            currSet.pop()

            helper(i+1, nums, currSet, subSets)

        helper(0, nums, currSet, subSets)

        return subSets
