class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")
        stack = []
        for e in arr:
            if e == "" or e == ".":
                pass
            elif e == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(e)
        return "/" + "/".join(stack)