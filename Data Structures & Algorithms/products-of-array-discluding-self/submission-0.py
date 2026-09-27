class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = []
        for i in range(len(nums)):
            rest = nums[:i] + nums[i+1:]
            total = 1
            for r in rest:
                total*=r
            res.append(total)
        return res     

