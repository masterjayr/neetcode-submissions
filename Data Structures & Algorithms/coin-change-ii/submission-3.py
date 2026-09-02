class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # using dp recipe
        # base case -> a == amount return 1 way - if i >= len(coins): return 0
        # state -> i, amount(0-amount)
        # choices -> dfs(i, amount +  coins[i]) + dfs(i+1, amount)
        # combine -> add them those are our choices

        # converting using dp recipe
        # dp = [[0] * (amount + 1) for i in range(len(coins) + 1)]
        dp = [0] * (amount + 1)
        dp[0] = 1
       

        for i in range(len(coins) - 1, -1, -1):
            nextDp = [0] * (amount + 1)
            nextDp[0] = 1
            for a in range(1, amount + 1):
                nextDp[a] = dp[a]
                if a - coins[i] >= 0:
                    nextDp[a] += nextDp[a-coins[i]]
            dp = nextDp
        return dp[amount]