class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left <= right:
            k = (left + right) // 2
            hours = 0

            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:
                right = k - 1
                res = min(res, k)

            else:
                left = k + 1
        return res