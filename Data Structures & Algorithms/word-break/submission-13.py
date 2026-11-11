class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            if i == len(s):
                return True

            for word in wordDict:
                length = i + len(word)

                if word == s[i:length]:
                    if dfs(length):
                        cache[i] = True
                        return cache[i]
            
            cache[i] = False
        
            return cache[i]

        return dfs(0)