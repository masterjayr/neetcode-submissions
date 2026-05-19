class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Trial With Caching
        cache = {0: 0}
        def dfs(amount, cache):
            if amount == 0:
                return 0

            if amount in cache:
                return cache[amount]

            res = 1e9
            for c in coins:
                if amount - c >= 0:
                    res = min(res, 1 + dfs(amount - c, cache))
            cache[amount] = res
            return cache[amount]

        minCoins = dfs(amount, cache)
        return -1 if minCoins >= 1e9 else minCoins

        