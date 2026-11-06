class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                length = i + len(w)
                if length <= len(s) and s[i:length] == w:
                    if dp[length]:
                        dp[i] = dp[length]
                        break
        return dp[0]