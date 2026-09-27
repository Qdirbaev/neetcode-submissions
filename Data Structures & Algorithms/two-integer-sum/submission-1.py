class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dick = {}
        for index, value in enumerate(nums):
            sec_val = target - value
            if sec_val not in dick:
                dick[value] = index
            else:
                sec_ind = dick[sec_val]
                return [sec_ind, index]