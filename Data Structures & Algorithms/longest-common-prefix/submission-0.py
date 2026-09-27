class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for index in range(len(prefix)):
            for word in strs[1:]:
                if len(word) == index or prefix[index] != word[index]:
                    return prefix[:index]
        return prefix