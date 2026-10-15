class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        longest = 0

        i = 0

        while i < len(nums):

            length = 1

            if nums[i] - 1 not in numSet:
                while nums[i] + length in numSet:
                    length += 1
                
                longest = max(longest, length)
            i += 1
        return longest