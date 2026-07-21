
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sCounter = Counter(s)

        for c in t:
            if sCounter[c] == 0:
                return False

            sCounter[c] -= 1
           

        return True 

  