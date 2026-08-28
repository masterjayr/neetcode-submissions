class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # state => r, c so 2D
        # base case => r == len(m)-1 and c == len(n)-1 : return 1
        # choices -> dfs(r+1, c) , dfs(r, c+1) if in bounds
        # combine -> + -> dfs(r+1, c) + dfs(r, c+1)
        # cache using dictionary
        cache = {}
        def dfs(r, c):
            if (r, c) in cache:
                return cache[(r,c)]

            if r == m-1 and c == n-1:
                return 1

            down = dfs(r+1, c) if r+1 < m else 0
            right = dfs(r, c+1) if c+1 < n else 0
            cache[(r,c)] = down + right

            return cache[(r, c)]


        # return dfs(0, 0)

        # converting using dp recipe
        # dp = [[1] * (n) for _ in range(m)]
        dp = [1] * n
        # base case is 1 but entire last row is 1 and entire last col is 1 but for learning i'll simulate this

        # above step is almost useless but yeah just for learning
        # start loop backwards
        for r in range(m-2, -1, -1):
            nextDp = [1] * n
            for c in range(n-2, -1, -1):
                # copy body of dfs
                down = dp[c]
                right = nextDp[c+1]
                nextDp[c] = down + right
            dp = nextDp
        return dp[0]
