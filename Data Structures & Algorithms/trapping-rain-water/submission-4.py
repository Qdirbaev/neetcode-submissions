class Solution:
    def trap(self, height: List[int]) -> int:
        left, right, res = [0], [0], 0
        left_top, right_top = 0, 0
        for i in range(len(height)):
            left.append(max(left_top, left[-1]))
            left_top = max(left_top, height[i])

            right.append(max(right_top, right[-1]))
            right_top = max(right_top, height[len(height) - i -1])
        for i in range(len(height)):
            temp = min(left[i+1], right[len(height) - i]) - height[i]
            if temp > 0:
                res += temp

        return res