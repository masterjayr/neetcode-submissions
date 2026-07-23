class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}

        def dfs(i):
            if i == len(s):
                return True 
            if i in cache:
                return cache[i]
            cache[i] = False
            for w in wordDict:
                if (i+len(w)) <= len(s) and s[i:i+len(w)] == w:
                    cache[i] = dfs(i + len(w))
                if cache[i]:
                    break

            return cache[i]

        return dfs(0)

        
