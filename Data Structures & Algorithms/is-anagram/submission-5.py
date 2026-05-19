class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charMap = {}

        for c in s:
            charMap[c] = charMap.get(c, 0) + 1

        for c in t:

            if c not in charMap:
                return False

            charMap[c] -= 1

            if charMap[c] == 0:
                del charMap[c]

        return True if not charMap else False