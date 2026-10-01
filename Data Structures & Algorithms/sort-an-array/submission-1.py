class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 0 or len(nums) == 1:
            return nums
        
        left = nums[:len(nums)//2]
        right = nums[len(nums)//2:]

        left = self.sortArray(left)
        right = self.sortArray(right)


        def merge(arr1, arr2):
            i, j, res = 0, 0, []

            while i < len(arr1) and j < len(arr2):
                if arr1[i] > arr2[j]:
                    res.append(arr2[j])
                    j+=1
                else:
                    res.append(arr1[i])
                    i+=1
            return res + arr1[i:] + arr2[j:]


        return merge(left, right)