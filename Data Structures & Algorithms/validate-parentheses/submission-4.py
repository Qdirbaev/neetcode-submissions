class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dick = {")": "(", "]": "[", "}": "{"}
        for bkt in s:
            if bkt in dick.values():
                stack.append(bkt)
            else: # if it's closing
                # 1st case if previous is opening
                if stack and stack[-1] == dick[bkt]:
                    stack.pop()
                else:
                    stack.append(bkt)
        return True if stack == [] else False