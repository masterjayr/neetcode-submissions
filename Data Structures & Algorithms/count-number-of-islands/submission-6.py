class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])

        visit = set()

        def dfs(r, c, visited):
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == "0":
                return

            grid[r][c] = "0"
            dfs(r+1, c, visited)
            dfs(r-1, c, visited)
            dfs(r, c+1, visited)
            dfs(r, c-1, visited)
        
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    res += 1
                    dfs(r, c, visit)

        return res