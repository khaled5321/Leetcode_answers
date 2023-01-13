class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for i in s:
            if i not in dic:
                stack.append(i)
                continue

            if not stack or dic[i] != stack[-1]:
                return False

            stack.pop()

        return not stack
