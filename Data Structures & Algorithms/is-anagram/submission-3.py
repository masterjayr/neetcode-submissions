class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}

        for st in s:
            freq[st] = freq.get(st, 0) + 1

        for st in t:
            if st not in freq:
                return False 

            freq[st] -= 1

            if freq[st] == 0:
                del freq[st]

        return False if freq else True

            