from collections import defaultdict
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = defaultdict(list)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)


        visit = set([beginWord])
        q = deque([beginWord])
        res = 1

        while q:
            for i in range(len(q)):
               word = q.popleft()
               if word == endWord:
                return res
               for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                for w in nei[pattern]:
                    if w not in visit:
                        visit.add(w)
                        q.append(w)

            res += 1
        
        return 0