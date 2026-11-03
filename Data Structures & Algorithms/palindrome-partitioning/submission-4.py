class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(i, currList):
            if i == len(s):
                res.append(currList.copy())
                return 

            for j in range(i, len(s)):
                string = s[i:j+1]
                if self.isPali(string):
                    currList.append(string)
                    dfs(j+1, currList)
                    currList.pop()

        dfs(0, [])
        return res

    def isPali(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l+=1
            r -= 1
        return True

            