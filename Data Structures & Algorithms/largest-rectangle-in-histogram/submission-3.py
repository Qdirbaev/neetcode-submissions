class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        top = 0

        for i, cur in enumerate(heights):
            if stk:
                start = i
                while stk and cur <= stk[-1][0]:
                    val, ind = stk.pop()
                    area = (i - ind) * val
                    top = max(top, area)
                    start = ind
                stk.append([cur, start])
            else:
                stk.append([cur, i])
        while stk:
            val, ind = stk.pop()
            area = (len(heights) - ind) * val
            top = max(top, area)
        return top
                