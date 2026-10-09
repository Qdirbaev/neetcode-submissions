class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r, top = 0, len(heights) - 1, 0

        while l < r:
            area = min(heights[l], heights[r]) * abs(l - r)
            top = max(top, area)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return top