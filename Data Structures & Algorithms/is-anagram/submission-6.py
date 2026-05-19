
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = {}

        for c in s:
            freq[c] = freq.get(c, 0) + 1

        for c in t:
            if c not in freq:
                return False

            if freq[c] == 0:
                return False

            freq[c] -= 1

        for val in freq.values():
            if val != 0:
                return False
        
        return True
  