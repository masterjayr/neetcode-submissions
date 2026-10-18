class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        tFreq = {}
        
        for c in t:
            tFreq[c] = tFreq.get(c, 0) + 1

        haves, needs = 0, len(tFreq)
        res, resLen = [-1, -1], float("inf")
        L = 0
        sFreq = {}
        for R in range(len(s)):
            c = s[R]
            sFreq[c] = sFreq.get(c, 0) + 1

            if c in tFreq and sFreq[c] == tFreq[c]:
                haves += 1

            while haves == needs:
                if R - L + 1 < resLen:
                    resLen = R - L + 1
                    res = [L, R]
                sFreq[s[L]] -= 1
                if s[L] in tFreq and sFreq[s[L]] < tFreq[s[L]]:
                    haves -= 1
                L+= 1
            
        L, R = res
        return s[L:R+1] if resLen != float("inf") else ""