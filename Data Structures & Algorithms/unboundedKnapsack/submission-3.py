class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # True DP Solution
        N, M = len(profit), capacity
        dp = [[-1] * (M + 1) for _ in range(N)]

        # initialize Columns
        for i in range(N):
            dp[i][0] = 0

        for c in range(M + 1):
            if weight[0] <= c:
                dp[0][c] = profit[0]

        for i in range(N):
            for c in range(M + 1):
                skip = dp[i-1][c]
                include = 0

                if c - weight[i] >= 0:
                    include = profit[i] + dp[i][c - weight[i]]
                
                dp[i][c] = max(skip, include)

        return dp[N-1][M]
        