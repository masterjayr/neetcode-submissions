class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # using dp recipe
        # base cases -> if i == len(s): return 0, if j == len(t): return 1
        # choices -> (i+1, j+1) + (i+1, j) if s[i] == t[j] else (i+1, j) 
        # combine -> add them up if matching 
        # state -> offcourse i, j 
        cache = {}
        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]

            if s[i] == t[j]:
                cache[(i,j)] = dfs(i+1, j+1) + dfs(i+1, j)

            else:
                cache[(i,j)] = dfs(i+1, j)

            return cache[(i, j)]


        return dfs(0, 0)