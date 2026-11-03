class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        digitsMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        output = []

        def dfs(currStr, i):
            if len(currStr) == len(digits):
                output.append(currStr)
                return
            # choices
            for c in digitsMap[digits[i]]:
                dfs(currStr + c, i+1)
        
        dfs("", 0)

        return output


            



