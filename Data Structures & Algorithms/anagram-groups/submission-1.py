class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lst = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            lst[key].append(word)
        return list(lst.values())