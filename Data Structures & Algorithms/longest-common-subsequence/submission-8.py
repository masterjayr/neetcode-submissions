class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:


        dp = [0] * (len(text2) + 1)

        for i in range(len(text1)-1, -1, -1):
            nextDp = [0] * (len(text2) + 1)
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    nextDp[j] = 1 + dp[j+1]
                else:
                    right = nextDp[j+1]
                    down = dp[j]
                    nextDp[j] = max(right, down)
            dp = nextDp
        return dp[0]
        