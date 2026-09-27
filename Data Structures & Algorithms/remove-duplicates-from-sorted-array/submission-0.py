class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for r in range(1, len(nums)):
            if nums[i] != nums[r]:
                i += 1
                nums[i] = nums[r]
        return i + 1