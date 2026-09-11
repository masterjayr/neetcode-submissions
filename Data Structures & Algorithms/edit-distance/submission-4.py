class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # using dp recipe
        # state -> i, j -> index word1, index word 2
        # base case -> i==len(word1) and j == len(word2): return 0
        # BASE CASE -> i == len(word1): return len(word2) - j
        # BASE CASE -> j == len(word2): return len(word1) - i
        # choices, (i+1, j+1) if match, (i, j+1), (i+1, j), (i+1, j+1)
        # combine -> 1 + min(choices) if no match meaning 1 op plus min operation to get to the end
        dp = {}
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i==len(word1) and j == len(word2):
                return 0
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            
            if word1[i] == word2[j]:
                dp[(i, j)] = dfs(i+1, j+1)
            else:
                diag = dfs(i+1, j+1)
                right = dfs(i, j+1)
                down = dfs(i+1, j)
                dp[(i,j)] = 1 + min(diag, right, down)
            return dp[(i,j)]
        return dfs(0, 0)