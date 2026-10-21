class Solution:
    def minWindow(self, s: str, t: str) -> str:

        tFreq = {}

        for c in t:
            tFreq[c] = tFreq.get(c, 0) + 1

        res, resLen = [-1, -1], float("inf")
        sFreq = {}

        have, need = 0, len(tFreq)

        L = 0

        for R in range(len(s)):
            c = s[R]
            sFreq[c] = sFreq.get(c, 0) + 1

            if c in tFreq and sFreq[c] == tFreq[c]:
                have += 1

            while have == need:
                if R - L + 1 < resLen:
                    res = [L, R]
                    resLen = (R - L + 1)
                c = s[L]
                sFreq[c] -= 1
                if c in tFreq and sFreq[c] < tFreq[c]:
                    have -= 1
                L += 1
        L, R = res
        return s[L:R+1] if resLen != float("inf") else ""
        