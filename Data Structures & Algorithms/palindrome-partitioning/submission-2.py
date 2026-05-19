class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def backtrack(i):

            if i == len(s):
                res.append(part.copy())
                return 

            # choices - all valid palindromes from i

            for j in range(i, len(s)):
                if self.isPali(i, j, s):
                    part.append(s[i:j+1])
                    backtrack(j+1)
                    part.pop()

            return res

        return backtrack(0)

    def isPali(self, l, r, s):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l+1, r - 1

        return True