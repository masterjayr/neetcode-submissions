class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if not nums:
            return [[]]

        perms = self.permute(nums[1:])
        res = []

        for p in perms:
            for i in range(len(p)+1):
                copy = p.copy()
                copy.insert(i, nums[0])
                res.append(copy)
        return res

