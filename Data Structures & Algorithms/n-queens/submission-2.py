class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        

        board = [["."] * n for i in range(n)]
        posDiag = set()
        negDiag = set()
        col = set()
        row = set()

        output = []

        def backtrack(r):
            if r == n:
                output.append(["".join(board[i]) for i in range(n)])
                return

            for c in range(n):
                if c in col or (r-c) in posDiag or (r+c) in negDiag or board[r][c] == "Q":
                    continue

                board[r][c] = "Q"
                posDiag.add((r-c))
                negDiag.add((r+c))
                col.add(c)

                backtrack(r+1)

                board[r][c] = "."
                posDiag.remove((r-c))
                negDiag.remove((r+c))
                col.remove(c)


        backtrack(0)

        return output

        