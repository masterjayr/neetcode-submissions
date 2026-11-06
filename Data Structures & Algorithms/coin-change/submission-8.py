class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # state=> amount
        # choices => all coins since i have unlimited number
        # base case amount == 0: return 1
        # min(res, 1 + dfs(amount - c))
        cache = {}
        def dfs(a):
            if a == 0:
                return 0
            if a in cache:
                return cache[a]
            res = amount + 1

            for c in coins:
                if a - c >= 0:
                    res = min(res, 1 + dfs(a-c))

            cache[a] = res

            return cache[a]
        ans = dfs(amount)
        return ans if ans != amount + 1 else -1
