class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        def dfs(i, curSubset):
            if i == len(nums):
                subsets.append(curSubset.copy())
                return

            curSubset.append(nums[i])
            dfs(i+1, curSubset)
            curSubset.remove(nums[i])
            dfs(i+1, curSubset)

        dfs(0, [])

        return subsets
