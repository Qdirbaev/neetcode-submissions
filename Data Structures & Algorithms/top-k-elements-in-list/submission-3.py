from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dick = Counter(nums)
        return [n for n, _ in dick.most_common(k)]