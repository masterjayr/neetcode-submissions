from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                currVal = board[r][c]
                if currVal == ".":
                    continue

                if currVal in cols[c] or currVal in rows[r] or currVal in squares[(r//3, c//3)]:
                    return False 
                

                cols[c].add(currVal)
                rows[r].add(currVal)
                squares[(r//3, c//3)].add(currVal)
        
        return True
                
                
