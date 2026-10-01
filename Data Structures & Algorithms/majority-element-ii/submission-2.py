from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = Counter(nums).most_common()
        return [x for x, freq in res if freq > len(nums)//3]