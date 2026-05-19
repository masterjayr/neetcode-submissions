class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT, window = {}, {}

        for c in t:
            countT[c] = countT.get(c, 0) + 1

        have, need = 0, len(countT)
        res, resLength = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]

            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:

                if (r - l + 1) < resLength:
                    res = [l, r]
                    resLength = (r - l + 1)

                # shrinking window now
                window[s[l]] -= 1
                # check if the character we are removing is
                # one of the ones we need and if so if it's 
                # count is less than the count in the countT
                # then we reduce have's by one and shrink Window (l+=1)
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res

        return s[l:r+1] if resLength != float("infinity") else ""
                

