class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # state -> i, j
        # choices -> word1[i] == word2[j]: dfs(i+1, j+1) no match? insert? dfs(i, j+1), delete dfs(i+1, j)
        # replace -> dfs(i+1, j+1)

        dp = {}
        def dfs(i, j):
            if i == len(word1) and j == len(word2):
                return 0
            
            if i == len(word1):
                return len(word2) - j
            
            if j == len(word2):
                return len(word1) - i

            if (i, j) in dp:
                return dp[(i,j)]

            if word1[i] == word2[j]:
                dp[(i,j)] = dfs(i+1, j+1)
            else:
                insert = dfs(i, j+1)
                delete = dfs(i+1, j)
                replace = dfs(i+1, j+1)
                dp[(i,j)] = 1 + min(insert, delete, replace)
            return dp[(i,j)]

        return dfs(0, 0)