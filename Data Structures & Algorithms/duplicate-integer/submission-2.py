class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dick = {}
        for num in nums:
            if num not in dick:
                dick[num] = 1
            else:
                return True
        return False