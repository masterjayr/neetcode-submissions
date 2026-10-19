class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minEating = float("inf")

        while l <= r:
            hours = (l + r) // 2
            total = 0
            for p in piles:
                total += math.ceil((p / hours))

            if total <= h:
                minEating = min(minEating, hours)
                r = hours - 1
            else:
                l = hours + 1

        return minEating
