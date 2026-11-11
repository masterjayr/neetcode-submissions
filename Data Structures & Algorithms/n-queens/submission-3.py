class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        cols = set()
        posDiag = set()
        negDiag = set()

        board = [["."] * n for i in range(n)]
        output = []

        def backtrack(r):
            if r == n:
                res = ["".join(board[i]) for i in range(n)]
                output.append(res)
                return

            for c in range(n):
                if r < 0 or c < 0 or r == n or c == n or c in cols or (r - c) in posDiag or (r + c) in negDiag:
                    continue
                
                board[r][c] = "Q"
                cols.add(c)
                posDiag.add(r-c)
                negDiag.add(r+c)

                backtrack(r + 1)
                
                board[r][c] = "."
                cols.remove(c)
                posDiag.remove(r-c)
                negDiag.remove(r+c)
        
        backtrack(0)

        return output
                