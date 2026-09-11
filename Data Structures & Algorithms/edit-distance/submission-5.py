class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # using dp recipe
        # state -> i, j -> index word1, index word 2
        # base case -> i==len(word1) and j == len(word2): return 0
        # BASE CASE -> i == len(word1): return len(word2) - j
        # BASE CASE -> j == len(word2): return len(word1) - i
        # choices, (i+1, j+1) if match, (i, j+1), (i+1, j), (i+1, j+1)
        # combine -> 1 + min(choices) if no match meaning 1 op plus min operation to get to the end
        dp = {}
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i==len(word1) and j == len(word2):
                return 0
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            
            if word1[i] == word2[j]:
                dp[(i, j)] = dfs(i+1, j+1)
            else:
                diag = dfs(i+1, j+1)
                right = dfs(i, j+1)
                down = dfs(i+1, j)
                dp[(i,j)] = 1 + min(diag, right, down)
            return dp[(i,j)]
        
        dp = [[float('inf')] * (len(word2) + 1) for i in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i
        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j

        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    diag = dp[i+1][j+1]
                    right = dp[i][j+1]
                    down = dp[i+1][j]
                    dp[i][j] = 1 + min(diag, right, down)
        return dp[0][0]









