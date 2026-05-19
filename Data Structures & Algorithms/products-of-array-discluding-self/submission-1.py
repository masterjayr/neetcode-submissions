class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums = [1,2,4,6]

        res = [1] * len(nums) # [1, 1, 1, 1]
        prefix = 1
        # loop through nums and calculate the prefix. basic idea is to ensure that 
        # each index contains the prefix product before it
        for i in range(len(nums)):
            res[i] = prefix # [1, 1, 2, 8]
            prefix *= nums[i]

        postfix = 1
        # loop backwards, multiplying the postfix by the val at res[i] which represents
        # the prefix product before it - aka, prefix * postfix
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

                

        