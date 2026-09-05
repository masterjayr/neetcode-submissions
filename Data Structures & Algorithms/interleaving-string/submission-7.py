class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # using dp recipe
        # state -> i, j (position s1, position s2)
        # base case -> i == len(s1) and j == len(s2): return True
        # choices -> if s1[i] == s3[i+j]: (i+1, j), s2[j] == s3[i+j]: (i, j+1)
        #combine -> dfs(i+1, j): return True immediately same with dfs(i, j+1)
        if len(s1) + len(s2) != len(s3): return False
        cache = {}
        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True
            if (i, j) in cache:
                return cache[(i,j)]

            if i < len(s1) and s1[i] == s3[i+j] and dfs(i+1, j):
                return True
            if j < len(s2) and s2[j] == s3[i+j] and dfs(i, j+1):
                return True

            cache[(i,j)] = False

            return cache[(i, j)]

        # return dfs(0, 0)

        dp = [[False] * (len(s2)+1) for i in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True # base case

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True
        
        return dp[0][0]




