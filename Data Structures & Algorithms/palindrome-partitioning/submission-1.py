class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curPart = []

        def dfs(i):
            if i >= len(s):
                res.append(curPart.copy())
                return

            # choices are all valid palindrome so we have to loop starting from i

            for j in range(i, len(s)):
                if self.isPali(i, j, s):
                    curPart.append(s[i:j+1])
                    dfs(j+1)
                    curPart.pop()

        dfs(0)
        return res
        
    def isPali(self, l, r, s):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l+1, r-1

        return True