class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}
        LIP = 0
        def dfs(r, c, prevVal):
            nonlocal LIP
            if (r < 0 or c < 0 or c == COLS or 
                r == ROWS or matrix[r][c] <= prevVal):
                    return 0

            if (r,c) in dp:
                return dp[(r,c)]

            res = 1 
            res = max(res, 1 + dfs(r+1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r-1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c+1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c-1, matrix[r][c]))
            dp[(r,c)] = res

            LIP = max(LIP, res)

            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)

        return LIP