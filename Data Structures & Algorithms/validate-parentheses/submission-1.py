class Solution:
    def isValid(self, s: str) -> bool:
        stacks = []
        opener = ['(', '[', '{']
        closer = [')', ']', '}']
        for i in s:
            if i in opener:
                stacks.append(i)
            elif stacks != [] and stacks[-1] == opener[closer.index(i)]:
                stacks.pop()
            else:
                stacks.append(i)
        return stacks == []