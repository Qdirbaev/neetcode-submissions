class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        cur_max = nums[0]
        l = 0
        r = k - 1

        while r < len(nums):
            if res:
                if nums[r] >= cur_max:
                    cur_max = nums[r]
                    res.append(cur_max)
                elif nums[l-1] == cur_max:
                    cur_max = max(nums[l:r+1])
                    res.append(cur_max)
                else:
                    res.append(cur_max)
            else:
                cur_max = max(nums[l:r+1])
                res.append(cur_max)
            l+=1
            r+=1
        return res