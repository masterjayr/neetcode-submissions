class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitsToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz" }

        def dfs(i, currStr):
            if len(currStr) == len(digits):
                res.append(currStr)
                return

            # going through all choices and capturing in currStr + c
            for c in digitsToChar[digits[i]]:
                dfs(i+1, currStr + c)

        
        if digits:
            dfs(0, "")

        return res










