class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = {}

        def dfs(i, j):
            if i < 0 or j == len(s):
                return 0

            if (i,j) in dp:
                return dp[(i,j)]

            

            if s[i] == s[j]:
                res = 1 if i == j else 2
                dp[(i,j)] = res + dfs(i - 1, j+1)
            else:
                dp[(i,j)] = max(dfs(i-1, j), dfs(i, j+1))

            return dp[(i, j)]

        for i in range(len(s)):
            dfs(i, i)
            dfs(i, i+1)

        return max(dp.values())
        