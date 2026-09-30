from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # {Counter: [word1, word2]}
        dick = {}
        for word in strs:
            count = Counter(word)
            key = tuple(sorted(count.items()))
            if key not in dick:
                dick[key] = [word]
            else:
                dick[key].append(word)
        return list(dick.values())


            