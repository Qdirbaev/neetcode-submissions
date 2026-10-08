import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def is_number(c):
            try:
                float(c)
                return True
            except ValueError:
                return 
        OPS = {"+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
            }
        for n in tokens:
            if is_number(n):
                stack.append(n)
            else:
                res = OPS[n](int(stack[-2]), int(stack[-1]))
                stack.pop()
                stack.pop()
                stack.append(res)
        return int(stack[-1])