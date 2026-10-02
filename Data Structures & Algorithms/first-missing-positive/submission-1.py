class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set(nums)
        k = 1
        while k in s:
            k+=1
        return k