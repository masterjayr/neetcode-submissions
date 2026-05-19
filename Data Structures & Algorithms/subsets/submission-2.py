class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []

        def backtrack(i, curSet):
            if i == len(nums):
                subset.append(curSet.copy())
                return 

            curSet.append(nums[i])
            backtrack(i+1, curSet)
            curSet.pop()

            backtrack(i+1, curSet)


        backtrack(0, [])
        return subset   
