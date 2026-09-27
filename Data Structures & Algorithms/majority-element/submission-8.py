class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dick = {}                
        for num in nums:
            dick[num] = dick.get(num, 0) + 1
            
        return max(dick, key=dick.get)