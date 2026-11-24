class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def dfs(i, a):
            if a == amount:
                return 1
            if i == len(coins) or a > amount:
                return 0
            if (i,a) in dp:
                return dp[(i,a)]

            dp[(i,a)] = dfs(i, a + coins[i]) + dfs(i+1, a)
            return dp[(i,a)]

        return dfs(0, 0)