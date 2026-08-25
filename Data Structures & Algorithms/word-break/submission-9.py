class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # using dp recipe
        # state - i 
        # choices -> every w in wordDict
        # validity -> if s[i:len(w)] == w - proceed next state 
        # next state -> i + len(w)
        # combine -> if dfs(i + len(w)) == True
        # base case -> i == len(s): return True

        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            if i == len(s):
                return True

            cache[i] = False
            # choices
            for w in wordDict:
                # valid choice
                if (i + len(w) <= len(s)) and s[i:i + len(w)] == w:
                    if dfs(i + len(w)):
                        cache[i] = True
                        break
                
            return cache[i]
        return dfs(0)