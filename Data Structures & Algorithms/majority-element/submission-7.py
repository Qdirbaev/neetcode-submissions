class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dick = {}                
        for num in nums:
            if num not in dick:
                dick[num] = 1
            else:
                dick[num] += 1
        value = max(list(dick.values()))
        key = next(k for k, v in dick.items() if v == value)
        return key