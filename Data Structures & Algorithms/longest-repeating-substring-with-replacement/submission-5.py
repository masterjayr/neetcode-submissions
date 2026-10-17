class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # so R-L+1 - max(freq.values()) > k:

        L = 0
        freq = {}
        longest = 0

        for R in range(len(s)):
            freq[s[R]] = freq.get(s[R], 0) + 1

            if ((R - L + 1) - max(freq.values())) <= k:
                longest = max(longest, (R - L + 1))
            else:
                freq[s[L]] -= 1
                L += 1
        
        return longest