class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = ["(", "[", "{"]
        closing = [")", "]", "}"]
        for bkt in s:
            if bkt in opening:
                stack.append(bkt)
            else: # if it's closing
                # 1st case if previous is opening
                if stack and stack[-1] in opening and opening.index(stack[-1]) == closing.index(bkt):
                    stack.pop()
                else:
                    stack.append(bkt)
        return True if stack == [] else False