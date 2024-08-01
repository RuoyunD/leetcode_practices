from collections import deque

class Solution:
    def decodeString(self, s: str) -> str:
        stack = deque()
        res = ""
        num = 0
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == "[":
                # 保存上一层的字符串和本层的重复次数
                stack.append((res, num))
                res = ""
                num = 0
            elif char == "]":
                prev_s, cur_num = stack.pop()
                res = prev_s + cur_num * res
            else:
                res += char
        return res
