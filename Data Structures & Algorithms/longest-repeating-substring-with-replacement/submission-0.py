class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0 

        l = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            # length of window - max count of letters > k - then
            # we don't have enough space to replace so we shrink
            # window.
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res