class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # part 1
        def first(matrix, target):
            l, r = 0, len(matrix) - 1
            while l <= r:
                m = (l + r) // 2
                if m == l:
                    if matrix[r][0] <= target:
                        return r
                    elif matrix[r][0] >= target:
                        return l
                    else:
                        return m
                elif matrix[m][0] < target:
                    l = m
                else:
                    r = m
            return False
        arr = matrix[first(matrix, target)]
        print(arr)
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (r + l) // 2
            if arr[m] < target:
                l = m + 1
            elif arr[m] > target:
                r = m - 1
            else:
                return True
        return False