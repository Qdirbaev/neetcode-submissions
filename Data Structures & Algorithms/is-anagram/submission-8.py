class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_dick = {}
        second_dick = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in first_dick:
                first_dick[s[i]] = 1
            else:
                first_dick[s[i]] += 1
            if t[i] not in second_dick:
                second_dick[t[i]] = 1
            else:
                second_dick[t[i]] += 1

        return first_dick == second_dick