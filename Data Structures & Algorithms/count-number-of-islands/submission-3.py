from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # key word is return number, not all as how backtracking says
        ROWS, COLS = len(grid), len(grid[0])
        neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        islands = 0
        visited = set()

        # def dfs(r, c):
        #     if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visited or grid[r][c] == "0":
        #         return 

        #     visited.add((r,c))
        #     dfs(r+1, c)
        #     dfs(r-1, c)
        #     dfs(r, c+1)
        #     dfs(r, c-1)
        q = deque()
        def bfs(r, c):
            q.append((r,c))
            while q:
                r, c = q.popleft()
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc

                    if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or (nr,nc) in visited or grid[nr][nc] == "0":
                        continue 

                    visited.add((nr,nc))
                    q.append((nr,nc))

        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c] == "1":
                    islands+=1
                    bfs(r,c)

        return islands

        