class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0


        for i in range(len(s)):
            l,r  = i, i
            res += self.helper(s, l, r)
            l, r = i, i+1
            res += self.helper(s, l, r)
        
        return res

    def helper(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res