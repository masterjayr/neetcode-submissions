class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # using dp recipe
        # state -> (i, buying/selling(bool))
        # base case -> i >= len(prices) -> nothing to buy or sell - return 0
        # choices buy -> dfs(i+1, sell) - prices[i], dfs(i+2, buy) sell -> dfs(i+2, buy) + prices[i], dfs(i+1, sell)
        # combine -> max of two choices each time
        
        dp = {}
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            # choices
            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                cooldown = dfs(i+1, buying)
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i+2, not buying) + prices[i]
                cooldown = dfs(i+1, buying)
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]

        return dfs(0, True)
