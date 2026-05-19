class Solution:
    def isValid(self, s: str) -> bool:
        closedToOpen = { ")": "(", "]":"[", "}":"{" }
        stack = []       
        for i in range(len(s)):

            if stack and s[i] in closedToOpen and stack[-1] == closedToOpen[s[i]]:
                stack.pop()
            else:
                stack.append(s[i])

        return True if stack == [] else False