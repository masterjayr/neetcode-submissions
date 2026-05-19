class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        candidates.sort()

        def helper(i, curSet, total):

            if total == target:
                res.append(curSet.copy())
                return

            if i == len(candidates) or total > target:
                return

            # first choice
            curSet.append(candidates[i])
            helper(i + 1, curSet, total+candidates[i])

            # second choice
            curSet.pop()

            # ensure to point i to the last duplicate
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            helper(i + 1, curSet, total)

        helper(0, [], 0)

        return res
