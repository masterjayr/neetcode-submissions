class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [1] * len(nums)

        prefixProd = [1] * len(nums)

        currPrefixProd = 1

        for i in range(len(nums)):
            output[i] = currPrefixProd
            currPrefixProd *= nums[i]

        currPostfixProd = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= currPostfixProd
            currPostfixProd *= nums[i]

        return output
        
