class Solution:
    def isValid(self, s: str) -> bool:
        closedToOpen = { ")": "(", "}": "{", "]": "[" }

        stack = []

        for i in s:

            if i in closedToOpen:
                if stack and closedToOpen[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return True if not stack else False