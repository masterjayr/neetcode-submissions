class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()
        def backtrack(i, currList, total):
            if total == target:
                res.append(currList.copy())
                return

            if i == len(candidates) or total > target:
                return

            currList.append(candidates[i])
            backtrack(i+1, currList, total + candidates[i])

            currList.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            backtrack(i+1, currList, total)

        backtrack(0, [], 0)

        return res

