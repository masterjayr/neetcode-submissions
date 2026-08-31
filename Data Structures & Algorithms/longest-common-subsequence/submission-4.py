class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # using recipe
        # state = i, j = i-> index of text1, j->index of text2
        # choices - if text1[i] == text[j] -> 1 + dfs(i+1, j+1) else max(dfs(i+1, j), dfs(i, j+1))
        # combine -> max and 1 + dfs(...)
        # base case -> i >= len(text1) or j >= len(text2)

        cache= {}
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i,j)]
            if i >= len(text1) or j >= len(text2):
                return 0
            
            if text1[i] == text2[j]:
                diag = dfs(i+1, j+1)
                cache[(i, j)] = 1 + diag
            else:
                down = dfs(i+1, j)
                right = dfs(i, j+1)
                cache[(i, j)] = max(down, right)


            return cache[(i, j)]

        # return dfs(0, 0)
        # converting to bottom up using dp recipe
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) -1, -1, -1):
                if text1[i] == text2[j]:
                    diag = dp[i+1][j+1]
                    dp[i][j] = 1 + diag
                else:
                    down = dp[i+1][j]
                    right = dp[i][j+1]
                    dp[i][j] = max(down, right)
        return dp[0][0]
            