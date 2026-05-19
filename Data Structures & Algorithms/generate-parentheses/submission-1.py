class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return 

            # choice 1
            if openN < n:
                stack.append("(")
                backtrack(openN+1, closedN)
                stack.pop()

            # choice 2
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)

        return res

