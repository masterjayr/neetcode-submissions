from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # key word is return number, not all as how backtracking says

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0


        # def dfs(r, c):
        #     if r < 0 or c < 0 or (r,c) in visited or r == ROWS or c == COLS or grid[r][c] == "0":
        #         return

        #     visited.add((r,c))
        #     choices 
        #     dfs(r+1, c)
        #     dfs(r-1, c)
        #     dfs(r, c+1)
        #     dfs(r, c-1)
        def bfs(r, c):
            queue = deque()
            queue.append((r,c))
            visited.add((r,c))
            neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            # go through choices
            while queue:
                r, c = queue.popleft()
                for dr, dc in neighbors:
                    nr, nc = dr+r, dc+c

                    if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or (nr, nc) in visited or grid[nr][nc] == "0":
                        continue

                    visited.add((nr,nc))
                    queue.append((nr,nc))
                    



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    islands+=1
                    bfs(r, c)

        return islands

        