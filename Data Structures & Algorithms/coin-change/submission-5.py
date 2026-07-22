class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Trial With Caching
        cache = {}
        def backtrack(amount):
            if amount == 0:
                return 0

            if amount in cache:
                return cache[amount]
            
            minCoin = float("inf")
            for c in coins:
                if amount - c >= 0:
                    result = backtrack(amount - c)
                    if result != -1:
                        minCoin = min(minCoin, 1 + result)
            
            cache[amount] = minCoin if minCoin != float("inf") else -1

            return cache[amount]

        return backtrack(amount)

