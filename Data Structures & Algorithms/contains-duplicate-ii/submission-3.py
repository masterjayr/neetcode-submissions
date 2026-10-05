class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        for L in range(len(nums)):
            for R in range(L+1, len(nums)):
                if R - L > k:
                    break

                if nums[L] == nums[R]:
                    return True

        return False
            