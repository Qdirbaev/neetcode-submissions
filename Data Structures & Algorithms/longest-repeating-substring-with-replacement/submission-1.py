class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        letters = [0] * 26

        for r in range(len(s)):
            letters[ord(s[r]) - 65] += 1
            while (r - l + 1) - max(letters) > k:
                letters[ord(s[l]) - 65] -=1
                l+=1
            longest = max(longest, (r-l + 1))
        return longest