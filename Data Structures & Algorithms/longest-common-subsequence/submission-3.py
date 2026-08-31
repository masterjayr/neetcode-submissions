class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # using recipe
        # state = i, j = i-> index of text1, j->index of text2
        # choices - if text1[i] == text[j] -> 1 + dfs(i+1, j+1) else max(dfs(i+1, j), dfs(i, j+1))
        # combine -> max and 1 + dfs(...)
        # base case -> i >= len(text1) or j >= len(text2)

        cache= {}
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i,j)]
            if i >= len(text1) or j >= len(text2):
                return 0
            
            if text1[i] == text2[j]:
                diag = dfs(i+1, j+1)
                cache[(i, j)] = 1 + diag

            else:
                down = dfs(i+1, j)
                right = dfs(i, j+1)
                cache[(i, j)] = max(down, right)


            return cache[(i, j)]

        return dfs(0, 0)
            