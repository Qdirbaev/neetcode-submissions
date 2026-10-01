class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = [1]*(len(nums)+1), [1]*(len(nums)+1)
        for index in range(len(nums)):
            left[index+1] = left[index] * nums[index]
        for i in range(len(nums), 0, -1): # 4, 3, 2, 1
            right[i-1] = right[i] * nums[i-1]
        res = []
        for i in range(len(nums)):
            res.append(left[i] * right[i+1])

        return res 
