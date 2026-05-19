from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)

        for s in strs:

            key = "".join(sorted(s))

            freq[key].append(s)

        return list(freq.values())