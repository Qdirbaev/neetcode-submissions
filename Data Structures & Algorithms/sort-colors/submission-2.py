class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # [1,0,1,2]
        # 1-iteration => [0, 1, 1, 2]
        for i in range(len(nums) - 1, 0, -1):  # 3, 2, 1
            for j in range(i): # 3, 2, 1
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]