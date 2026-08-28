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


        return dfs(0, 0)

