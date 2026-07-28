class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0] * (n + 1) for _ in range(m + 1)]

        def dfs(r, c):
            if r == m and c == n:
                return 1
            if r > m or c > n:
                return 0
            if cache[r][c] != 0:
                return cache[r][c]

            cache[r][c] = dfs(r+1, c) + dfs(r, c + 1)

            return cache[r][c]


        dp = [[0] * (n + 1) for _ in range(m+1)]

        for r in range(m+1):
            dp[r][n] = 1

        for r in range(m, 0, -1):
            for c in range(n-1, 0, -1):
                
                down = dp[r+1][c] if (r+1) <= m else 0
                right = dp[r][c+1] if (c+1) <= n else 0
                dp[r][c] = down + right

        return dp[1][1]

        # space optimized 
        row = [0] * n

        for i in range(m):
            newRow = [1] * n
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]


