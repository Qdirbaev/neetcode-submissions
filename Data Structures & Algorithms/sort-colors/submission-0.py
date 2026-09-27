from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        dick = Counter(nums) #Counter({1: 2, 0: 1, 2: 1})
        # [0, 1, 1, 2]
        # 0   1  2   3
        r, w, b = dick[0], dick[1], dick[2] # 1, 2, 1

        for red in range(r):
            nums[red] = 0
        for white in range(r, w + r):
            nums[white] = 1
        for blue in range(w + r, w + r + b):
            nums[blue] = 2

        