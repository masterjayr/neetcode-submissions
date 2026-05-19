from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        maxArea = 0

        def dfs(r, c):
            if (
                        r < 0 or c < 0 or
                        r >= ROWS or c >= COLS or
                        (r, c) in visited or
                        grid[r][c] == 0
                    ):
                        return 0

            
            visited.add((r,c))
            res = 1
            res += dfs(r+1, c)
            res += dfs(r-1, c)
            res += dfs(r, c+1)
            res += dfs(r, c-1)

            return res

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxArea = max(maxArea, dfs(r, c))

        return maxArea
