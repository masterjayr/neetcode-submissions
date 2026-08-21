class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Trial With Caching
        
        # state -> amount
        # base condition amount == 0: return 0
        # choices -> all coins since we can use unlimited number of times so amount - coin >= 0
        # combine -> min(between all choices)
        cache = {}
        def dfs(amount):
            if amount in cache:
                return cache[amount]
            if amount == 0:
                return 0 # 0 coins

            res = float('inf')
            # choices
            for c in coins:
                if amount - c >= 0:
                    res = min(res, 1 + dfs(amount - c))
            cache[amount] = res
            return cache[amount]

        # ans = dfs(amount)
        # return ans if ans != float('inf') else -1

        # Top down
        # init dp with any initializations inside the dfs function
        dp = [float("inf")] * (amount + 1)
        # base case
        dp[0] = 0

        for a in range(1, amount + 1): # signifies my dfs(amount) function going from big amount to small so starting at amount 7 to 0 in reverse i'm starting from amount 1 to amount since and base case amount 0 is already set
            # choices now same as dfs replaced with dp
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        
        return dp[amount] if dp[amount] != float("inf") else -1














