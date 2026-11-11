class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                    length = i + len(word)

                    if word == s[i:length]:
                        if dp[length]:
                            dp[i] = True
        
        return dp[0]
                            

        