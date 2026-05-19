class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity
        dp = [[0] * (M + 1) for _ in range(N)]

        # setup
        for r in range(N):
            dp[r][0] = 0

        for c in range(M+1):
            if weight[0] <= c:
                dp[0][c] = profit[0]

        
        for r in range(N):
            for c in range(M+1):
                skip = dp[r-1][c]

                #include
                include = 0
                if c - weight[r] >= 0:
                    include = profit[r] + dp[r-1][c - weight[r]]

                dp[r][c] = max(include, skip)

        return dp[N-1][M]

    