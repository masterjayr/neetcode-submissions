class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqMap = {}

        for st in s:
            freqMap[st] = freqMap.get(st, 0) + 1 

        for st in t:
            if st not in freqMap:
                return False 

            if st in freqMap:
                freqMap[st] -= 1

                if freqMap[st] == 0:
                    del freqMap[st]
        return False if freqMap else True

            