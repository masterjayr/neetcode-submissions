class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.word = True

    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])

        root = TrieNode()
        visited = set()
        res = set()
        for w in words:
            root.addWord(w)

        def dfs(r, c, node, curWord):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visited or board[r][c] not in node.children:
                return
            
            visited.add((r,c))
            char = board[r][c]
            curWord += char
            node = node.children[char]
            if node.word:
                res.add(curWord)
            
            dfs(r+1, c, node, curWord)
            dfs(r-1, c, node, curWord)
            dfs(r, c+1, node, curWord)
            dfs(r, c-1, node, curWord)

            visited.remove((r,c))

        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)

