class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()

        L = 0
        longest = 0

        for R in range(len(s)):
            while s[R] in window:
                window.remove(s[L])
                L += 1
                continue

            window.add(s[R])
            longest = max(longest, R - L + 1)

        return longest
