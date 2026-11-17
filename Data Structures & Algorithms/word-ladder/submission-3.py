class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        nei = defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                pattern = w[:i] + "*" + w[i+1:]
                nei[pattern].append(w)

        q = collections.deque([beginWord])
        visit = set([beginWord])
        res = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for w in nei[pattern]:
                        if w not in visit:
                            visit.add(w)
                            q.append(w)

            res += 1
        return 0