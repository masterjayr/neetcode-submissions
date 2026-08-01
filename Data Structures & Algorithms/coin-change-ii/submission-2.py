class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}

        def dfs(i, a):
            if a == amount:
                return 1
            if i == len(coins):
                return 0
            if a > amount:
                return 0
            if (i, a) in cache:
                return cache[(i, a)]
            
            cache[(i,a)] = dfs(i, a + coins[i]) + dfs(i+1, a)

            return cache[(i,a)]

        # dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        # for i in range(len(coins) + 1):
        #     dp[i][0] = 1
        # for i in range(len(coins)-1, -1, -1):
        #     for a in range(amount + 1):
        #         dp[i][a] = dp[i+1][a]
        #         if a - coins[i] >= 0:
        #             dp[i][a] += dp[i][a-coins[i]]

        # return dp[0][amount]

        # space optimized way
        dp = [0] * (amount + 1)
        dp[0] = 1 

        for i in range(len(coins)-1, -1, -1):
            nextDp = [0] * (amount + 1)
            nextDp[0] = 1
            for a in range(amount + 1):
                nextDp[a] = dp[a]
                if a - coins[i] >= 0:
                    nextDp[a] += nextDp[a - coins[i]]
            dp = nextDp
        return dp[amount]

        

        