class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for l in s:
            if l != "]":
                stack.append(l)
            else:
                res = ''
                while stack and stack[-1] != '[':
                    res = stack.pop() + res
                stack.pop()
                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                stack.append(int(k)*res)
        return "".join(stack)