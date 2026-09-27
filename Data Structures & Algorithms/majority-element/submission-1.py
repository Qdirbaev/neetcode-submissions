class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dick = {}
        for num in nums:
            if num not in dick.keys():
                dick[num] = 1
            else:
                dick[num] += 1
        max_value = max(dick.values())
        for key, val in dick.items():
            if max_value == val:
                return key