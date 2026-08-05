class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}

        def dfs(i, j):
            if i == len(word1):
                return len(word2) - j 
            if j == len(word2):
                return len(word1) - i

            if (i, j) in cache:
                return cache[(i, j)]

            if word1[i] == word2[j]:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            else:
                right = dfs(i, j+1)
                down = dfs(i+1, j)
                diagonal = dfs(i+1, j+1)
                cache[(i,j)] = 1 + min(right, down, diagonal)

                return cache[(i, j)]

        # return dfs(0, 0)

        dp = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

        # initialize base cases 
        for j in range(len(word2)+1):
            dp[len(word1)][j] = len(word2) - j 
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i

        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2) -1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    right = dp[i][j+1]
                    down = dp[i+1][j]
                    diagonal = dp[i+1][j+1]
                    dp[i][j] = 1 + min(right, down, diagonal)

        return dp[0][0]
