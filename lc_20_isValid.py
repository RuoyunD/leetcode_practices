from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for i in range(0, len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            if s[i] == ")":
                if not stack or stack.pop() != '(':
                    return False
            if s[i] == "]":
                if not stack or stack.pop() != '[':
                    return False
            if s[i] == "}":
                if not stack or stack.pop() != '{':
                    return False
        return len(stack) == 0
