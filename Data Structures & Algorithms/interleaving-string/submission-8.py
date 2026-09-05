class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # using dp recipe
        # state -> i, j (position s1, position s2)
        # base case -> i == len(s1) and j == len(s2): return True
        # choices -> if s1[i] == s3[i+j]: (i+1, j), s2[j] == s3[i+j]: (i, j+1)
        #combine -> dfs(i+1, j): return True immediately same with dfs(i, j+1)
        if len(s1) + len(s2) != len(s3): return False
        # dp = [[False] * (len(s2)+1) for i in range(len(s1) + 1)]
        dp = [False] * (len(s2)+1)
        dp[len(s2)] = True # base case

        for i in range(len(s1), -1, -1):
            nextDp = [False] * (len(s2)+1)

            for j in range(len(s2), -1, -1):
                if i == len(s1) and j==len(s2):
                    nextDp[j] = True
                if i < len(s1) and s1[i] == s3[i+j] and dp[j]:
                    nextDp[j] = True
                if j < len(s2) and s2[j] == s3[i+j] and nextDp[j+1]:
                    nextDp[j] = True
            dp = nextDp
        return dp[0]






