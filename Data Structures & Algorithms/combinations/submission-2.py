class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        comb = []
        def helper(i, n, k, currComb, comb):
            if len(currComb) == k:
                comb.append(currComb[:])
                return 

            if i > n:
                return

            for j in range(i, n+1):
                currComb.append(j)
                helper(j+1, n, k, currComb, comb)
                currComb.pop()

        helper(1, n, k, [], comb)

        return comb