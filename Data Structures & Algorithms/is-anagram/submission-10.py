class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}

        for c in s:
            sMap[c] = sMap.get(c, 0) + 1

        for c in t:
            if c not in sMap:
                return False
            
            sMap[c] -= 1
            if sMap[c] == 0:
                del sMap[c]

        return True if not sMap else False