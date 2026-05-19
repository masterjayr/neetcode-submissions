class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        def dfs(i, curSet):

            if i == len(nums):
                subsets.append(curSet.copy())
                return

            # first choice
            curSet.append(nums[i])
            dfs(i+1, curSet)
            
            # second choice
            curSet.pop()
            dfs(i+1, curSet)
        dfs(0, [])
        return subsets
