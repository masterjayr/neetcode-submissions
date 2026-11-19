class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = [[0]*(amount+1) for i in range(len(coins) + 1)]

        for r in range(len(coins)):
            dp[r][0] = 1

        for i in range(len(coins)-1, -1, -1):
            for a in range(1, amount + 1):
                dp[i][a] = dp[i+1][a]
                if a - coins[i] >= 0:
                    dp[i][a] += dp[i][a - coins[i]]
        return dp[0][amount]