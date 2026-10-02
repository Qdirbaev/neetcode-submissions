class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        arr = []
        for num in nums:
            k = 0
            if (num - 1) not in s:
                # constantly check for num+k, if finds k++
                while num + k in s:
                    k += 1
            arr.append(k)
        res = 0 if arr == [] else max(arr)
        return res