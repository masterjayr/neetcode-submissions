class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        while l <= r:

            m = (l + r) // 2

            if nums[m] == target:
                return m

            # we are at the left side
            if nums[m] >= nums[l]:

                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1

            # we are on the right side
            else:
                if target > nums[r] or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1


        return -1
