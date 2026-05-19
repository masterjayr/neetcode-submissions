class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mapIndex = {}
        output = []
        # mapIndex = {0: 1, 1: 2, 2:4, 3: 6}
        for idx, val in enumerate(nums):
            mapIndex[idx] = val

        for i in range(len(nums)):
            prod = 1
            for key, v in mapIndex.items():
                if i == key:
                    continue

                prod *= v
            
            output.insert(i, prod)

        return output
                

        