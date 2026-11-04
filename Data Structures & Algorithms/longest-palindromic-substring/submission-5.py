class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        longest = 0
        res = ""

        for i in range(len(s)):

            l, r = i, i

            while l >= 0 and r < len(s) and l <= r:
                if s[l] == s[r]:
                    if (r - l + 1) > longest:
                        longest = r - l + 1
                        res = s[l:r+1]

                    l -= 1
                    r += 1
                else:
                    break
            

            l, r = i, i+1
            while l >= 0 and r < len(s) and l <= r:
                if s[l] == s[r]:
                    if (r - l + 1) > longest:
                        longest = r - l + 1
                        res = s[l:r+1]
                    
                    l -= 1
                    r += 1
                else:
                    break

        return res