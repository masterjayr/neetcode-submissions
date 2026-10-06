class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # naive approach
        # if not s:
        #     return 0

        # length = 1
        # for L in range(len(s)):
        #     window = set()
        #     window.add(s[L])
        #     for R in range(L+1, len(s)):
        #         if s[R] in window:
        #             break

        #         window.add(s[R])

        #         length = max(length, R - L + 1)
        
        # return length

        # optimized
        L = 0
        window = set()
        length = 0

        for R in range(len(s)):
            while s[R] in window:
                window.remove(s[L])
                L += 1

            window.add(s[R])
            length = max(length, R - L + 1)

        return length