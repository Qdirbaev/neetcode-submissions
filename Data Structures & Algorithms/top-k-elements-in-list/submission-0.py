from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        # counter then sort it based on values, then get last k elements
        dick = Counter(nums) # Counter({3: 3, 2: 2, 1: 1})
        sorted_dick = dict(sorted(dick.items(), key=lambda x: x[1])) # {1: 1, 2: 2, 3: 3}

        for _ in range(k):
            res.append(list(sorted_dick.keys())[-1])
            deleted = sorted_dick.popitem()
        return res