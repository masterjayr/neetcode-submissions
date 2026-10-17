class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = [0] * 26
        s2Count = [0] * 26

        for i in range(len(s1)):
            idx1 = ord(s1[i]) - ord('a')
            idx2 =ord(s2[i]) - ord('a')
            s1Count[idx1] += 1
            s2Count[idx2] += 1

        matches = sum(1 for i in range(26) if s1Count[i] == s2Count[i])

        for R in range(len(s1), len(s2)):
            if matches == 26:
                return True

            idx = ord(s2[R]) - ord('a')

            s2Count[idx] += 1

            if s2Count[idx] == s1Count[idx]:
                matches += 1
            elif s2Count[idx] == s1Count[idx] + 1:
                matches -= 1
            
            L = R - len(s1)
            idx = ord(s2[L]) - ord('a')
            s2Count[idx] -= 1
            if s2Count[idx] == s1Count[idx]:
                matches += 1
            elif s2Count[idx] == s1Count[idx] -1:
                matches -= 1
        return matches == 26



