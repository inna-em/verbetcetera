class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] == target or row[-1] == target:
                return True
            if row[0] < target and row[-1] > target:
                l, r = 0, len(matrix[0])
                while l < r:
                    m = (l + r)//2
                    if row[m] == target:
                        return True
                    elif row[m] < target:
                        l = m + 1
                    else:
                        r = m - 1
                if row[l] == target:
                    return True
        return False
